import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import joblib
from src.utils.config import *

df = pd.read_csv(RESULT_PATH)

# Train probability baseline
prob_model = XGBClassifier(n_estimators=300, max_depth=6)
prob_model.fit(df[FEATURES], df["conversion"])
joblib.dump(prob_model, MODEL_P_PATH)

df["probability"] = prob_model.predict_proba(df[FEATURES])[:,1]

# Strategy ranking
random_df = df.sample(frac=1).reset_index(drop=True)
prob_df = df.sort_values("probability", ascending=False).reset_index(drop=True)
uplift_df = df.sort_values("uplift", ascending=False).reset_index(drop=True)

def evaluate(strategy_df):
    max_users = BUDGET // COST_PER_USER
    selected = strategy_df.iloc[:max_users]
    incremental_revenue = (selected["uplift"] * PROFIT_PER_CONVERSION).sum()
    roi = incremental_revenue / BUDGET
    negative_rate = (selected["uplift"] < 0).mean()
    return incremental_revenue, roi, negative_rate

rand_rev, rand_roi, rand_neg = evaluate(random_df)
prob_rev, prob_roi, prob_neg = evaluate(prob_df)
upl_rev, upl_roi, upl_neg = evaluate(uplift_df)

results = pd.DataFrame({
    "Strategy": ["Random","Probability","Uplift"],
    "Incremental Revenue": [rand_rev, prob_rev, upl_rev],
    "ROI": [rand_roi, prob_roi, upl_roi],
    "Negative Target Rate": [rand_neg, prob_neg, upl_neg]
})

results.to_csv(STRATEGY_PATH, index=False)

print(results)

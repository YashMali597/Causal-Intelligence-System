import pandas as pd
import numpy as np
from src.utils.config import DATA_PATH

np.random.seed(42)
n = 150000

df = pd.DataFrame({
    "user_id": range(n),

    "sessions_30d": np.random.poisson(18, n),
    "avg_session_time": np.random.normal(8, 2, n),
    "pages_viewed": np.random.poisson(25, n),

    "transactions_30d": np.random.poisson(4, n),
    "avg_order_value": np.random.normal(60, 15, n),
    "days_since_last_purchase": np.random.randint(0, 60, n),

    "churn_risk_score": np.random.uniform(0,1,n),

    "emails_opened": np.random.poisson(3, n),
    "push_clicks": np.random.poisson(2, n),

    "subscription_tier": np.random.choice([0,1,2], n),
    "region": np.random.choice([0,1,2,3], n)
})

df["treatment"] = np.random.binomial(1, 0.5, n)

# Smooth base probability
base_prob = (
    0.005 * df["sessions_30d"] +
    0.01 * df["transactions_30d"] -
    0.3 * df["churn_risk_score"] +
    0.003 * df["pages_viewed"]
)

base_prob += np.random.normal(0, 0.03, n)

# Smooth heterogeneous treatment effect
treatment_effect = (
    0.02 * df["emails_opened"] +
    0.015 * df["push_clicks"] -
    0.02 * df["churn_risk_score"]
)

treatment_effect += np.random.normal(0, 0.02, n)

df["prob_control"] = base_prob.clip(0, 1)
df["prob_treated"] = (base_prob + treatment_effect).clip(0, 1)

df["conversion"] = np.where(
    df["treatment"] == 1,
    np.random.binomial(1, df["prob_treated"]),
    np.random.binomial(1, df["prob_control"])
)

df.to_csv(DATA_PATH, index=False)

print("Realistic smooth dataset generated.")

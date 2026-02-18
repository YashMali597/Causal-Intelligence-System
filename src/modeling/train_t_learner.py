import pandas as pd
from xgboost import XGBClassifier
import joblib
from src.utils.config import *

df = pd.read_csv(DATA_PATH)

treated = df[df["treatment"]==1]
control = df[df["treatment"]==0]

model_t = XGBClassifier(n_estimators=300, max_depth=6)
model_c = XGBClassifier(n_estimators=300, max_depth=6)

model_t.fit(treated[FEATURES], treated["conversion"])
model_c.fit(control[FEATURES], control["conversion"])

joblib.dump(model_t, MODEL_T_PATH)
joblib.dump(model_c, MODEL_C_PATH)

print("T-Learner trained.")

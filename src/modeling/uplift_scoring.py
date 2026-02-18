import pandas as pd
import joblib
from src.utils.config import *

df = pd.read_csv(DATA_PATH)

model_t = joblib.load(MODEL_T_PATH)
model_c = joblib.load(MODEL_C_PATH)

uplift = (
    model_t.predict_proba(df[FEATURES])[:,1] -
    model_c.predict_proba(df[FEATURES])[:,1]
)

df["uplift"] = uplift
df.to_csv(RESULT_PATH, index=False)

print("Uplift scoring completed.")

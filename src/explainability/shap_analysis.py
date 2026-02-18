import pandas as pd
import shap
import joblib
from src.utils.config import *

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_T_PATH)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(df[FEATURES])

shap.summary_plot(shap_values, df[FEATURES])

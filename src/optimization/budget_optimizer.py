import pandas as pd
from src.utils.config import *

def optimize_budget(budget):
    df = pd.read_csv(RESULT_PATH)
    df = df.sort_values("uplift", ascending=False)
    max_users = budget // COST_PER_USER
    selected = df.iloc[:max_users]
    incremental_revenue = (selected["uplift"] * PROFIT_PER_CONVERSION).sum()
    roi = incremental_revenue / budget
    return incremental_revenue, roi

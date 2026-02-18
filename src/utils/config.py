DATA_PATH = "data/uplift_experiment_data.csv"
RESULT_PATH = "data/uplift_results.csv"
STRATEGY_PATH = "data/strategy_results.csv"

MODEL_T_PATH = "data/model_t.joblib"
MODEL_C_PATH = "data/model_c.joblib"
MODEL_P_PATH = "data/probability_model.joblib"

FEATURES = [
    "sessions_30d",
    "avg_session_time",
    "pages_viewed",
    "transactions_30d",
    "avg_order_value",
    "days_since_last_purchase",
    "churn_risk_score",
    "emails_opened",
    "push_clicks",
    "subscription_tier",
    "region"
]


BUDGET = 100000
COST_PER_USER = 5
PROFIT_PER_CONVERSION = 100

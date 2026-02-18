import pandas as pd
from src.optimization.budget_optimizer import optimize_budget

budgets = [25000, 50000, 75000, 100000, 150000]

results = []

for budget in budgets:
    revenue, roi = optimize_budget(budget)
    results.append({"Budget": budget, "Incremental Revenue": revenue, "ROI": roi})

print(pd.DataFrame(results))

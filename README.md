━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀  CAUSAL INTELLIGENCE SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
type: "Budget-Constrained Growth Optimization Engine"
category: "Causal Targeting | Experimentation Intelligence"

core_idea:
  problem: >
    Traditional ML predicts who will convert.
    This system predicts who converts because of intervention.

  solution: >
    Estimate individual treatment effects from randomized A/B data
    and allocate marketing budget to high-impact persuadable users.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊  IMPACT (150,000-User A/B Simulation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

budget_scenario: "$100,000 fixed campaign budget"

roi_comparison:
  Random_Targeting: "1.3x ROI"
  Probability_Targeting: "2.6x ROI"
  Uplift_Targeting: "6.8x ROI (heterogeneous scenario)"

quantified_results:
  incremental_revenue: "$684,000+ captured"
  roi_improvement_vs_probability: "+161%"
  negative_target_reduction: "0% negative-impact users selected"
  revenue_efficiency: "Majority of incremental revenue captured in top 10–20% users"

evaluation_standard:
  method: "Observed treatment-control outcome comparison"
  validation: "No circular uplift validation"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠  METHODOLOGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

modeling:
  approach: "T-Learner (XGBoost)"
  objective: "Heterogeneous Treatment Effect Estimation"
  formula: "ITE = P(Y|T=1,X) − P(Y|T=0,X)"

comparison_strategies:
  - "Random Allocation"
  - "Conversion Probability Targeting"
  - "Uplift-Based Targeting"

analysis:
  - "Revenue Efficiency Curve"
  - "Marginal Revenue Capture"
  - "Customer Persuadability Segmentation"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🖥  INTERACTIVE DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

features:
  - "Dynamic Budget Slider"
  - "Real-time ROI Recalculation"
  - "Revenue Efficiency Curve (% Targeted vs Revenue)"
  - "Strategy ROI Comparison"
  - "Persuadability Segmentation"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠  TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  - Python
  - XGBoost
  - Dash
  - Plotly


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡  KEY INSIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Predicting conversion probability is not enough.

  Optimizing for incremental causal impact
  under budget constraints drives superior ROI.



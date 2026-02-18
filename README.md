project:
  name: "🚀 Causal Intelligence System"
  tagline: "📈 Budget-Constrained Growth Optimization Engine"

overview:
  description: >
    🔍 A production-style causal targeting system that identifies persuadable users
    from randomized A/B experiments and optimizes marketing allocation
    under fixed budget constraints.

  core_difference: >
    ❗ Traditional ML predicts who will convert.
    ✅ This system predicts who converts *because of intervention*.

experiment:
  scale_users: 150000
  experiment_type: "Randomized A/B Simulation"
  treatment_split: "50% Treatment / 50% Control"
  campaign_budget_usd: 100000
  profit_per_conversion_usd: 100
  cost_per_user_usd: 5

impact:
  roi_comparison:
    random_targeting: "1.3x"
    probability_targeting: "2.6x"
    uplift_targeting: "6.8x (heterogeneous scenario)"
    roi_improvement_vs_probability_percent: 161

  incremental_revenue_usd: 684000
  negative_target_reduction_percent: 100
  revenue_efficiency:
    insight: >
      ⚡ Majority of incremental revenue captured
      within the top 10–20% of uplift-ranked users.

evaluation:
  method: "📊 Observed treatment-control outcome comparison"
  validation_type: "Offline policy evaluation"
  circular_uplift_validation_used: false
  budget_constrained_evaluation: true

methodology:
  modeling_strategy: "🧠 T-Learner"
  algorithm: "XGBoost"
  objective: "Heterogeneous Treatment Effect Estimation"
  treatment_effect_formula: "ITE = P(Y|T=1,X) − P(Y|T=0,X)"

  strategies_compared:
    - "🎲 Random Allocation"
    - "📊 Conversion Probability Targeting"
    - "🚀 Uplift-Based Targeting"

dashboard:
  features:
    - "🎛 Interactive budget slider"
    - "📈 Real-time ROI recalculation"
    - "📊 Revenue efficiency curve (% targeted vs revenue)"
    - "🔄 Strategy comparison (Random vs Probability vs Uplift)"
    - "👥 Customer persuadability segmentation"
    - "🌙 Executive dark theme UI"

technology_stack:
  language: "Python"
  libraries:
    - "XGBoost"
    - "Dash"
    - "Plotly"
    - "Pandas"
    - "NumPy"

demonstrated_capabilities:
  - "🧠 Causal inference modeling"
  - "📈 Heterogeneous treatment effect estimation"
  - "💰 Budget allocation o

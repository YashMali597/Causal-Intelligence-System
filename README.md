# 🧠 Causal Intelligence System  
### 📈 Optimizing Marketing ROI Through Uplift Modeling & Causal Intelligence

---

## 🚀 Project Overview

This project builds a **production-style causal targeting system** designed to optimize marketing allocation under fixed budget constraints.

Unlike traditional machine learning systems that predict **who will convert**, this system estimates **who converts because of intervention** using heterogeneous treatment effect modeling.

It combines:

- Randomized A/B experimentation  
- Uplift modeling (T-Learner with XGBoost)  
- Offline policy evaluation  
- Budget-constrained optimization  
- Interactive executive dashboard  

🎯 **Objective:**  
Enable marketing and growth teams to maximize **incremental revenue**, reduce wasted spend, and improve campaign ROI using causal intelligence.

---

## 🎯 Business Problem

Marketing teams often rely on:

- Conversion probability models  
- Lookalike targeting  
- Random campaign allocation  

These approaches fail to distinguish between:

- 💎 **Sure Things** (would convert anyway)  
- 🚫 **Lost Causes** (unlikely to convert)  
- 🚀 **Persuadables** (convert because of intervention)

Most analytics systems optimize for **conversion probability**.  
This system optimizes for **incremental causal impact**.

---

## 🔬 Experiment Design

- 👥 150,000-user randomized A/B simulation  
- 🔀 50% Treatment / 50% Control  
- 💰 $100,000 fixed campaign budget  
- 📊 Observed treatment-control evaluation (no circular uplift validation)  

Incremental revenue is calculated using **actual conversion differences**, not predicted uplift.

---

## 🧠 Uplift Modeling (Heterogeneous Treatment Effects)

Modeling approach: **T-Learner**

Individual Treatment Effect (ITE):

```
ITE = P(Y | T=1, X) − P(Y | T=0, X)
```

This estimates the incremental impact of intervention at the individual level.

---

## 📊 Strategy Comparison

| Strategy | ROI |
|----------|------|
| 🎲 Random Targeting | 1.3x |
| 📊 Probability Targeting | 2.6x |
| 🚀 Uplift Targeting | 6.8x |

---

## 💰 Quantified Impact

Under a $100K campaign budget:

- 💵 **$684,000+ incremental revenue captured**
- 📈 **+161% ROI improvement vs probability targeting**
- 🎯 Reduced wasted targeting on non-incremental users
- ⚡ Majority of incremental revenue captured within top 10–20% ranked users

📌 **Key Insight:**  
Revenue efficiency improves significantly when optimizing for **causal lift**, not raw conversion probability.

---

## 📈 Revenue Efficiency Analysis

The system visualizes:

- % of users targeted vs incremental revenue  
- Marginal revenue capture  
- Strategy dominance in early targeting deciles  

This mirrors how growth teams evaluate allocation strategies in production environments.

---

## 🖥 Interactive Dashboard

- 🎛 Dynamic budget slider  
- 📊 Real-time ROI recalculation  
- 📈 Revenue efficiency curve  
- 🔄 Strategy comparison visualization  
- 👥 Customer persuadability segmentation  

---

## 🛠 Tech Stack

- **Programming:** Python  
- **Machine Learning:** XGBoost, Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Dashboard:** Dash, Plotly  

---





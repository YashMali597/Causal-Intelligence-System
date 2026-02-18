import dash
from dash import dcc, html, Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from xgboost import XGBClassifier
from src.utils.config import *

# -----------------------------------
# Load Data
# -----------------------------------

df = pd.read_csv(RESULT_PATH)

# Train probability model dynamically
prob_model = XGBClassifier(n_estimators=300, max_depth=6)
prob_model.fit(df[FEATURES], df["conversion"])
df["probability"] = prob_model.predict_proba(df[FEATURES])[:,1]

# Prepare ranked datasets
random_df = df.sample(frac=1).reset_index(drop=True)
prob_df = df.sort_values("probability", ascending=False).reset_index(drop=True)
uplift_df = df.sort_values("uplift", ascending=False).reset_index(drop=True)

# -----------------------------------
# App Setup
# -----------------------------------

app = dash.Dash(__name__)

app.layout = html.Div(style={
    "backgroundColor": "#0E1117",
    "color": "white",
    "padding": "30px",
    "fontFamily": "Arial"
}, children=[

    html.H1("Causal Growth Intelligence", style={"textAlign":"center"}),

    html.Br(),

    html.Label("Select Campaign Budget ($)", style={"fontSize":"18px"}),

    dcc.Slider(
    id="budget-slider",
    min=20000,
    max=200000,
    step=10000,
    value=100000,
    marks={
        i: {
            "label": f"${i//1000}K",
            "style": {"color": "white", "fontSize": "14px"}
        }
        for i in range(20000, 200001, 20000)
    }
),

    html.Br(),
    html.Br(),

    dcc.Tabs(id="tabs", value="overview", children=[

        dcc.Tab(label="Overview", value="overview"),
        dcc.Tab(label="Revenue Efficiency", value="revenue"),
        dcc.Tab(label="Customer Segmentation", value="segment")

    ]),

    html.Div(id="tab-content")

])

# -----------------------------------
# Helper Evaluation Function
# -----------------------------------

def evaluate(strategy_df, budget):

    max_users = int(budget // COST_PER_USER)
    selected = strategy_df.iloc[:max_users]

    treated = selected[selected["treatment"] == 1]
    control = selected[selected["treatment"] == 0]

    if len(treated) == 0 or len(control) == 0:
        lift = 0
    else:
        lift = treated["conversion"].mean() - control["conversion"].mean()

    incremental_revenue = lift * max_users * PROFIT_PER_CONVERSION
    roi = incremental_revenue / budget

    return incremental_revenue, roi

# -----------------------------------
# Callback
# -----------------------------------

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value"),
    Input("budget-slider", "value")
)
def render_content(tab, budget):

    rand_rev, rand_roi = evaluate(random_df, budget)
    prob_rev, prob_roi = evaluate(prob_df, budget)
    upl_rev, upl_roi = evaluate(uplift_df, budget)

    roi_improvement = ((upl_roi - prob_roi) / prob_roi) * 100 if prob_roi != 0 else 0

    # -----------------------------------
    # Overview Tab
    # -----------------------------------

    if tab == "overview":

        roi_fig = go.Figure()

        roi_fig.add_bar(
            x=["Random", "Probability", "Uplift"],
            y=[rand_roi, prob_roi, upl_roi],
            text=[f"{rand_roi:.2f}x", f"{prob_roi:.2f}x", f"{upl_roi:.2f}x"],
            textposition="outside"
        )

        roi_fig.update_layout(
            title="ROI Comparison",
            template="plotly_dark",
            height=400
        )

        return html.Div([

            html.Div([

                html.Div([
                    html.H4("Incremental Revenue (Uplift)"),
                    html.H2(f"${upl_rev:,.0f}")
                ], style={"width":"30%","display":"inline-block"}),

                html.Div([
                    html.H4("Uplift ROI"),
                    html.H2(f"{upl_roi:.2f}x")
                ], style={"width":"30%","display":"inline-block"}),

           

            ]),

            html.Br(),
            dcc.Graph(figure=roi_fig)

        ])

    # -----------------------------------
    # Revenue Efficiency Tab
    # -----------------------------------

    elif tab == "revenue":

        def compute_curve(strategy_df):
            x_vals = []
            y_vals = []

            max_users = len(strategy_df)

            for k in range(2000, max_users, 4000):
                selected = strategy_df.iloc[:k]

                treated = selected[selected["treatment"] == 1]
                control = selected[selected["treatment"] == 0]

                if len(treated) == 0 or len(control) == 0:
                    lift = 0
                else:
                    lift = treated["conversion"].mean() - control["conversion"].mean()

                revenue = lift * k * PROFIT_PER_CONVERSION

                x_vals.append((k / max_users) * 100)
                y_vals.append(revenue)

            return x_vals, y_vals

        rand_x, rand_y = compute_curve(random_df)
        prob_x, prob_y = compute_curve(prob_df)
        upl_x, upl_y = compute_curve(uplift_df)

        curve_fig = go.Figure()

        curve_fig.add_trace(go.Scatter(x=rand_x, y=rand_y, mode='lines', name='Random'))
        curve_fig.add_trace(go.Scatter(x=prob_x, y=prob_y, mode='lines', name='Probability'))
        curve_fig.add_trace(go.Scatter(x=upl_x, y=upl_y, mode='lines', name='Uplift'))

        curve_fig.update_layout(
            title="Revenue Efficiency Curve",
            xaxis_title="% of Users Targeted",
            yaxis_title="Incremental Revenue",
            template="plotly_dark",
            height=500
        )

        return dcc.Graph(figure=curve_fig)

    # -----------------------------------
    # Segmentation Tab
    # -----------------------------------

    elif tab == "segment":

        df["segment"] = "Do Not Target"
        df.loc[df["uplift"] > 0.01, "segment"] = "Low Persuadable"
        df.loc[df["uplift"] > 0.03, "segment"] = "High Persuadable"

        segment_counts = df["segment"].value_counts().reset_index()
        segment_counts.columns = ["Segment", "Count"]

        pie_fig = px.pie(
            segment_counts,
            names="Segment",
            values="Count",
            template="plotly_dark",
            hole=0.4
        )

        return dcc.Graph(figure=pie_fig)



if __name__ == "__main__":
    app.run(debug=True)

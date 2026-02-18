import plotly.express as px

def roi_bar(results):
    return px.bar(results, x="Strategy", y="ROI",
                  title="ROI Comparison Across Strategies")

def revenue_bar(results):
    return px.bar(results, x="Strategy", y="Incremental Revenue",
                  title="Incremental Revenue Comparison")

def uplift_distribution(df):
    return px.histogram(df, x="uplift",
                        title="Uplift Distribution")

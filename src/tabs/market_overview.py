import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Generate dummy stock market data
dates = pd.date_range(start="2024-01-01", periods=100, freq="D")
prices = np.cumsum(np.random.randn(100)) + 100

df = pd.DataFrame({"date": dates, "price": prices})

# Layout
layout = dbc.Container(
    [
        html.H2("Market Overview"),
        dcc.Graph(id="stock-price-chart"),
    ]
)


# Callbacks
def register_callbacks(app):
    @app.callback(
        dash.Output("stock-price-chart", "figure"),
        dash.Input("stock-price-chart", "id"),
    )
    def update_chart(_):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=df["date"], y=df["price"], mode="lines", name="Stock Price")
        )
        fig.update_layout(
            title="Stock Market Prices", xaxis_title="Date", yaxis_title="Price"
        )
        return fig

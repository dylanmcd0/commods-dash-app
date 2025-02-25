import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        html.H2("Commodities Dashboard"),
        html.P("This page will display various commodity prices and trends."),
        dcc.Graph(id="commodities-chart"),
    ]
)


def register_callbacks(app):
    @app.callback(
        dash.Output("commodities-chart", "figure"),
        dash.Input("commodities-chart", "id"),
    )
    def update_chart(_):
        return {"data": [], "layout": {"title": "Commodity Prices"}}

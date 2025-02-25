import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        html.H2("Economic Indicators"),
        html.P(
            "Placeholder for economic data like GDP, inflation, and employment rates."
        ),
        dcc.Graph(id="economic-indicators-chart"),
    ]
)


def register_callbacks(app):
    @app.callback(
        dash.Output("economic-indicators-chart", "figure"),
        dash.Input("economic-indicators-chart", "id"),
    )
    def update_chart(_):
        return {"data": [], "layout": {"title": "Economic Data"}}

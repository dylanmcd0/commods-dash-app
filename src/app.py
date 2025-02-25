import dash
from dash import dcc, html
import plotly.graph_objects as go

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Needed for deployment

# Layout
app.layout = html.Div(
    children=[
        html.H1("Commodity Analysis Dashboard", style={"textAlign": "center"}),
        html.P("Tracking Oil & Gas Market Trends", style={"textAlign": "center"}),
        dcc.Graph(
            id="example-chart",
            figure=go.Figure(data=[go.Scatter(y=[1, 3, 2, 4], x=[1, 2, 3, 4])]),
        ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

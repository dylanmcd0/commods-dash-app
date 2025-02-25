import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from tabs import market_overview, commodities, economic_indicators

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Commodity Dashboard", className="ms-2"),
            dbc.Nav(
                [
                    dbc.NavLink(
                        "About Me", href="/", active="exact", className="nav-link-hover"
                    ),
                    dbc.NavLink(
                        "Market Overview",
                        href="/market-overview",
                        active="exact",
                        className="nav-link-hover",
                    ),
                    dbc.NavLink(
                        "Commodities Dashboard",
                        href="/commodities",
                        active="exact",
                        className="nav-link-hover",
                    ),
                    dbc.NavLink(
                        "Economic Indicators",
                        href="/economic-indicators",
                        active="exact",
                        className="nav-link-hover",
                    ),
                ],
                className="ms-auto",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    sticky="top",
)

# Define the home page
home_layout = html.Div(
    className="home-container",
    children=[
        html.Div(
            children=[
                html.H4("Welcome to My Page", className="glow-text"),
                html.P(
                    "Sort of a random project for when I have free time to develop my own analysis of commodity markets,"
                    " trading insights, and economic indicators, presented with a sleek, futuristic interface."
                ),
                html.P("WARNING: I suck at front-end development"),
            ],
            className="home-content",
        )
    ],
)

# Define the app layout
app.layout = dbc.Container(
    [dcc.Location(id="url", refresh=False), navbar, html.Div(id="page-content")],
    fluid=True,
)


# Callback to switch between pages
@app.callback(dash.Output("page-content", "children"), dash.Input("url", "pathname"))
def render_page(pathname):
    if pathname == "/market-overview":
        return market_overview.layout
    elif pathname == "/commodities":
        return commodities.layout
    elif pathname == "/economic-indicators":
        return economic_indicators.layout
    else:
        return home_layout  # Default to Home Page


# Register callbacks
market_overview.register_callbacks(app)
commodities.register_callbacks(app)
economic_indicators.register_callbacks(app)

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)

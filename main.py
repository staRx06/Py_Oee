import dash
import dash_daq as daq
from dash import dcc as dcc
from dash import html as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("D:/Data/Dashboard/New folder/data.csv", low_memory=False)
# data = data.query("OEE")
data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%y")
data.sort_values("Date", inplace=True)

A = (data["AVAILABILITY"].mean() * 100)
P = (data["PERFORMANCE"].mean() * 1000)
Q = (data["QUALITY"].mean() * 100)
OEE = (data["OEE"].mean() * 10)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "OEE_app.title"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📈", className="header-emoji"),
                html.H1(
                    children="OEE Report", className="header-title"
                ),
                html.P(
                    children="OEE Analyse",
                    className="header-description",
                ),
            ],
            className="header",
        ),

        # html.Div(
        #     children=[
        #         html.Div(
        #             children=[
        #                 html.Div(children="Region", className="menu-title"),
        #                 dcc.Dropdown(
        #                     id="region-filter",
        #                     options=[
        #                         {"label": region, "value": region}
        #                         for region in np.sort(data.region.unique())
        #                     ],
        #                     value="Albany",
        #                     clearable=False,
        #                     className="dropdown",
        #                 ),
        #             ]
        #         ),
        #         html.Div(
        #             children=[
        #                 html.Div(children="Type", className="menu-title"),
        #                 dcc.Dropdown(
        #                     id="type-filter",
        #                     options=[
        #                         {"label": avocado_type, "value": avocado_type}
        #                         for avocado_type in data.type.unique()
        #                     ],
        #                     value="organic",
        #                     clearable=False,
        #                     searchable=False,
        #                     className="dropdown",
        #                 ),
        #             ],
        #         ),
        #         html.Div(
        #             children=[
        #                 html.Div(
        #                     children="Date Range",
        #                     className="menu-title"
        #                 ),
        #                 dcc.DatePickerRange(
        #                     id="date-range",
        #                     min_date_allowed=data.Date.min().date(),
        #                     max_date_allowed=data.Date.max().date(),
        #                     start_date=data.Date.min().date(),
        #                     end_date=data.Date.max().date(),
        #                 ),
        #             ]
        #         ),
        #     ],
        #     className="menu",
        # ),
        #

        html.Div(
            children=[
                html.Div(
                    children=daq.Gauge(
                        showCurrentValue=True,
                        color={"gradient": True, "ranges": {"green": [0, 60], "yellow": [60, 80], "red": [80, 100]}},
                        # id='my-gauge-1',
                        label="A(%)",
                        value=A,
                        max=100,
                        min=0,
                    ),
                    className="card",
                ),

                html.Div(
                    children=daq.Gauge(

                        showCurrentValue=True,
                        color={"gradient": True, "ranges": {"green": [0, 60], "yellow": [60, 80], "red": [80, 100]}},
                        # id='my-gauge-1',
                        label="P(%)",
                        value=P,
                        max=100,
                        min=0,
                    ),
                    className="card",
                ),

                html.Div(
                    children=dcc.Graph(
                        id="OEE-Report",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["OEE"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

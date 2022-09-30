import dash
import dash_daq as daq
from dash import dcc as dcc
from dash import html as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input


data = pd.read_csv("D:/Data/Dashboard/New folder/dt1.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

# A=(data["AVAILABILITY"].mean()*100)
# P=(data["PERFORMANCE"].mean()*1000)
# Q=(data["QUALITY"].mean()*100)
# OEE=(data["OEE"].mean()*10)

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

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Reports", className="menu-title"),
                        dcc.Dropdown(
                            options= [
                                {'label': OEE, 'value': OEE}
                                for OEE in np.sort(data.OEE)
                                # {'label':"AVAILABILITY", 'value': "AVAILABILITY"},
                                # {'label':"PERFORMANCE", 'value': "PERFORMANCE"},
                                # {'label':"QUALITY", 'value': "QUALITY"},
                                ],
                            # data.columns,
                            id="report-filter",
                            # value="OEE",
                            clearable=False,
                            className="dropdown",
                            placeholder="Select a Data"

                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=
                    dcc.Graph(
                        id="oee-report",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)
@app.callback(
    [Output("oee-report", "figure")],
    [
        Input("report-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(coluu, start_date, end_date):
    mask = (
        (data.OEE == coluu)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    data_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["OEE"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>%",
            },
        ],
        "layout": {
            "title": {
                "text": "Average",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "%", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }
    return [data_chart_figure]
#---------------------------------------------------------------------------------------------
    #
    # data_gauge_figure = {
    #     "data": [
    #         {
    #             "x": filtered_data["Date"],
    #             "y": filtered_data["Total Volume"],
    #             "type": "lines",
    #         },
    #     ],
    #     "layout": {
    #         "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
    #         "xaxis": {"fixedrange": True},
    #         "yaxis": {"fixedrange": True},
    #         "colorway": ["#E12D39"],
    #     },
    # }

# ---------------------------------------------------------------
#     return data_chart_figure


#---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run_server(debug=True)

import dash_daq as daq
from dash import Dash, html, dcc, Input, Output
import pandas as pd

df=pd.read_csv("D:/Data/Dashboard/New folder/data.csv", low_memory=False)
A=(df["AVAILABILITY"].mean()*100)
P=(df["PERFORMANCE"].mean()*100)
Q=(df["QUALITY"].mean()*100)
OEE=(df["OEE"].mean()*10)

app = Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
        #id='my-gauge-1',
        label="OEE(%)",
        value=OEE,
        max = 100,
        min = 0,
    ),

    daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
        #id='my-gauge-1',
        label="A(%)",
        value=A,
        max = 100,
        min = 0,
    ),

    daq.Thermometer(
        min=95,
        max=105,
        value=100,
        showCurrentValue=True,
        units="C"
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
import plotly.graph_objs as go
from plotly.subplots import make_subplots as ms
import pandas as pd

df=pd.read_csv("D:/Data/Dashboard/New folder/data.csv")
A=(df["AVAILABILITY"].mean()*100)
P=(df["PERFORMANCE"].mean()*1000)
Q=(df["QUALITY"].mean()*100)
OEE=(df["OEE"].mean()*10)
trace1 = go.Indicator(mode="gauge+number",    value=A,    domain={'x': [0.0, 0.2], 'y': [0.15, 1]}, title={'text': "A(%)"})
trace2 = go.Indicator(mode="gauge+number",    value=P,    domain={'x': [0.3, 0.5], 'y': [0.15, 1]}, title={'text': "P(%)"})
trace3 = go.Indicator(mode="gauge+number",    value=Q,    domain={'x': [0.6, 0.8], 'y': [0.15, 1]}, title={'text': "Q(%)"})
trace4 = go.Indicator(mode="gauge+number",    value=OEE,    domain={'x': [0.3, 0.5], 'y': [0.8, 1]}, title={'text': "OEE(%)"})

layout = go.Layout(height = 600,
                   width = 600,
                   autosize = False,
                   title = 'OEE report')
fig = go.Figure(data = [trace1, trace2, trace3,trace4], layout = layout)

fig.show()

# print(A,P,Q,OEE)

#Q---Dash-----------------------


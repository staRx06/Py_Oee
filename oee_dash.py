import plotly.graph_objs as go
from plotly.subplots import make_subplots


#Quality_starts
T_J= float(input("Total job produced : "))        # total jobs
R_J= float(input("Nos of rejected jobs : "))        # rejected jobs
G_C= T_J-R_J                                        # Good count
Q= (G_C/T_J)*100                                    # Quality = good count/ total count

#Availablity_starts

NAT= 8              #Net available time
DWN_T= float(input("Down Time : "))                 # Down_time
UP_T = NAT-DWN_T                                    # Up_time
A=(((UP_T)/NAT)*100)                              # Availablity
print("Up time = ",UP_T)

# Performance_starts
ACT = ((UP_T/T_J)*3600)                             # Actual Cycle Time
SCT= 9.0                                            # Standard Cycle Time
P = ((SCT/ACT)*100)                                     # Performance
"""

print("Availability percentage : {:.2f} %".format(A))
print("Performance percentage : {:.2f} % ".format(P))
print("Quality percentage : {:.2f} %".format(Q))
"""
OEE = (A*P*Q)/10000
# print("OEE is : {:.2f} %".format(OEE))

#---Dash-----------------------


trace1 = go.Indicator(mode="gauge+number",    value=A,    domain={'x': [0.0, 0.2], 'y': [0.15, 1]}, title={'text': "A(%)"})
trace2 = go.Indicator(mode="gauge+number",    value=P,    domain={'x': [0.3, 0.5], 'y': [0.15, 1]}, title={'text': "P(%)"})
trace3 = go.Indicator(mode="gauge+number",    value=Q,    domain={'x': [0.6, 0.8], 'y': [0.15, 1]}, title={'text': "Q(%)"})
trace4 = go.Indicator(mode="gauge+number",    value=OEE,    domain={'x': [0.3, 0.5], 'y': [0.8, 1]}, title={'text': "OEE(%)"})

layout = go.Layout(height = 600,
                   width = 600,
                   autosize = False,
                   title = 'Side by side gauge diagrams')
fig = go.Figure(data = [trace1, trace2, trace3,trace4], layout = layout)

fig.show()
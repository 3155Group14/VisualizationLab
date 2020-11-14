import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data - This creates three scatter charts with the corresponding data and stores them in the data array
# for later use.
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temperature')
trace2 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean Temperature')
trace3 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Minimum Temperature')
data = [trace1,trace2,trace3]

# Preparing layout
layout = go.Layout(title='Max, min, and mean temperatures from 7/1/2014 to 6/9/2015', xaxis_title="Date",
                   yaxis_title="Temperatures")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherMultilinechart.html')
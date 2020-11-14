import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

df = df.sort_values('actual_max_temp',ascending=True)
# Preparing data - Creates heatmap using heatmap function and x,y,z values from our csv file.
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['actual_max_temp'].tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Recorded max temperature on day of week and month of year', xaxis_title="Day of Week",
                   yaxis_title="Month of Week")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherHeatmap.html')
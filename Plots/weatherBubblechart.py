import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')


# Creating sum of number of cases group by Country Column
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()

# Preparing data - This creates a scatter plot suitable for bubble charts (Mode = 'markers").
data = [go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_min_temp'],color=new_df['average_max_temp'], showscale=True))]

# Preparing layout
layout = go.Layout(title='Average min and max temperature of each month', xaxis_title="Average Minimum Temperature",
                   yaxis_title="Average Maximum Temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherBubblechart.html')
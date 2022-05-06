import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('mobilebrands.csv')

fig = ff.create_distplot([df['Avg Rating']], ['Avg Rating'])
fig.show()
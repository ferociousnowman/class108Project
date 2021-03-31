import pandas as pd 
import csv
import plotly.figure_factory as ff

df=pd.read_csv('data1.csv')
AvgRating=df['Avg Rating'].tolist()
fig=ff.create_distplot([AvgRating],['AvgRating'],show_hist=False)
fig.show()
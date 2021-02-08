import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
avg_rating = list(df["Avg Rating"])

fig = ff.create_distplot([avg_rating], ["Average Rating"], show_hist=False)
fig.show()

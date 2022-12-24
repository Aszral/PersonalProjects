import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("IPL 2022.csv")
print(data.head())

figure = px.bar(data, x=data["match_winner"],
                title="Number of Matches Won in IPL 2022")
figure.show()

data["won_by"] = data["won_by"].map({"Wickets": "Chasing", "Runs": "Defending"})

won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue', 'yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

figure = px.bar(data, x=data["top_scorer"],
                title="Top Scorers in IPL 2022")
figure.show()

figure = px.bar(data, x=data["top_scorer"], y=data["highscore"], color=data["highscore"],
                title="Top Scorers in IPL 2022")
figure.show()

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['./assets/stlesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

fig_px = px.scatter(x=[0,1,2,3,4], y=[2,4,6,7,9])
fig_go = go.Figure(data=[
    go.Scatter(x=[0,1,2,3,4], y=[2,4,6,7,9], mode='markers'),
    go.Scatter(x=[0,1,2,3,4], y=[9,7,6,4,2], mode='markers')
])
fig_go.add_trace(go.Scatter(x=[0,1,2,3,4], y=[19,17,16,14,12], mode='markers'))
fig_go_df= go.Figure(data=[
    go.Scatter(x=data['Postal'], y=data['Population'], mode='markers')
])

app.layout = html.Div([
    html.H1('Our first plot', id='header'),
    dcc.Graph(
        id='graph',
        figure={
            'data':[
                {'x': [1,2,3], 'y': [4,1,2]}
            ],
            'layout':{
                'title': 'Cool new plot'
            }
        }
    ),
    dcc.Graph(
        id='graph_px',
        figure=fig_px
    ),
    dcc.Graph(
        id='graph_go',
        figure=fig_go
    ),
    dcc.Graph(
        id='graph_go_df',
        figure=fig_go_df
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

external_stylesheets = ['src/assets/stlesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#https://population.un.org/wpp/Download/Standard/CSV/
data = pd.read_csv('src/assets/data.csv')

app.layout = html.Div([
    html.H1('World population indicators', id='header'),
    dcc.Dropdown(id='dropdown_countries', options=[
        {'label': country, 'value': country} for country in data['Location'].unique()
    ]),
    html.P(id='country_chosen')
])

@app.callback(
    Output('country_chosen', 'children'),
    [Input('dropdown_countries', 'value')]
)
def show_selected_country(dropdown_countries_value):
    return dropdown_countries_value


if __name__ == "__main__":
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

external_stylesheets = ['src/assets/stlesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#https://population.un.org/wpp/Download/Standard/CSV/
data = pd.read_csv('./assets/data.csv')

app.layout = html.Div([
    html.H1('World population indicators', id='header'),
    dcc.Dropdown(id='dropdown_countries', multi=True,
                 options=[
                    {'label': country, 'value': country} for country in data['Location'].unique()
                ],
                value=['Germany']
    ),
    dcc.Checklist(id='checklist_indicators', options=[
        {'label': 'Life expectancy at birth for both sexes combined (years)', 'value': 'LEx'},
        {'label': 'Male life expectancy at birth (years)', 'value': 'LExMale'},
        {'label': 'Female life expectancy at birth (years)', 'value': 'LExFemale'}
    ],
                  inputStyle={"margin-right": "15px", "margin-top": "10px"},
                  style={"padding": "20px"},
                  value=['LEx']),
    dcc.Graph(id='plot_lex'),
    dcc.RangeSlider(id='rangeslider_lex', min=0, max=29, step=1, value=[0,29],
                    allowCross=False, updatemode='drag',
                    marks={i: '{}'.format(time) for i, time in enumerate(data['MidPeriod'].unique())})
])

@app.callback(
    Output('plot_lex', 'figure'),
    [Input('checklist_indicators', 'value'),
     Input('dropdown_countries', 'value'),
     Input('rangeslider_lex', 'value')]
)
def show_selected_country(checklist_indicators_value, dropdown_countries_value, rangeslider_lex_value):
    fig = go.Figure()
    if checklist_indicators_value is None or dropdown_countries_value is None:
        return fig
    for country in dropdown_countries_value:
        df_country = data.loc[data['Location'] == country]
        df_country = df_country.iloc[rangeslider_lex_value[0]:rangeslider_lex_value[1], :]
        for indicator in checklist_indicators_value:
            fig.add_trace(go.Scatter(x=df_country['MidPeriod'], y=df_country[indicator], name=country + " " + indicator))
    fig.update_layout(showlegend=True)
    return fig



if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
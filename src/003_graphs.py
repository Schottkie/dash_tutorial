import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

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
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)
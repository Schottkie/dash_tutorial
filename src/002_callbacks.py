import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Our first dash app', id='header'),
    html.Button('Click me to change header', id='button', n_clicks=0),
    html.P('', id='last_header')
])

#Output only as list when there are multiple outputs
@app.callback(
    [Output('header', 'children'),
    Output('last_header', 'children')],
    [Input('button', 'n_clicks')],
    [State('header', 'children')]
)
def update_output(button_n_clicks, header_children):
    return 'The button was clicked {} times'.format(button_n_clicks), header_children


if __name__ == "__main__":
    app.run_server(debug=True)
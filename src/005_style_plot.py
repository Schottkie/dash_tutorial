import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['./assets/stlesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#TODO styling graphs

app.layout = html.Div([])


if __name__ == "__main__":
    app.run_server(debug=True)
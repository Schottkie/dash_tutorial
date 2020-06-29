import dash
import dash_html_components as html

app = dash.Dash(__name__)

# html = <h1>Our first dash app</h1>
app.layout = html.H1('Our first dash app')

if __name__ == "__main__":
    app.run_server(debug=True)
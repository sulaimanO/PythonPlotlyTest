import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# create dash
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(children=[])

if __name__ == '__main__':
    app.run_server(debug=True)

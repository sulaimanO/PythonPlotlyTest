import plotly.express as px
import services.general_data as gt
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html

df = gt.get_table_of_all_data()[0]

def all_data_pie(options, label):
    return html.Div([
        html.Div([
            html.Label([label]),
            dcc.Dropdown(
                id='my_dropdown',
                options=options,
                value='gender',
                multi=False,
                clearable=False,
                style={"width": "100%"}
            ),
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ]),

    ])


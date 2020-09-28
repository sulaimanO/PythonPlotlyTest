import plotly.express as px
import services.general_data as gt
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html

df = gt.get_table_of_all_data()[0]

def active_inactive_dropdown_list():
    return html.Div([
        html.Div([
            html.Label(['select from the list below']),
            dcc.Dropdown(
                id='my_dropdown',
                options=[
                    {"label": 'Gender', "value": 'gender'},
                    {"label": 'Country', "value": 'Country'},
                    {"label": 'Job Title', "value": 'JobTitle'},
                    {"label": 'State', "value": 'State'},
                    {"label": 'Work Active', "value": 'WorkActive'},

                ],
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

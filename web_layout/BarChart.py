#https://plotly.com/python/bar-charts/
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import services.general_data as gt
import numpy as np


# does not show data right
def relation_between_job_and_state_and_gender():
    #df = gt.get_table_of_all_data()[0]
   #print(gt.get_countries()[1])
    #fig = px.bar(df, x="Country", y="State", color="State", barmode="group")

    return html.Div([
        dcc.Dropdown(
            id='active_state_dropdown',
            options=[
                {"label": 'Gender', "value": 'gender'},
                {"label": 'Job Title', "value": 'JobTitle'},
                {"label": 'Work Active', "value": 'WorkActive'},
            ],
            multi=True,
            value="gender"
        ),
        html.Div([
            dcc.Graph(id='the_active_state_graph')
        ]),
    ])

# relation between job and state and gender
def dropdwon_selected_job_state_gender(value):
    x = None
    y = None
    color = None

    # if user not select y and color
    if isinstance(value, str):
        print('here 1')
        x = value
        y = 'JobTitle'
        color = 'WorkActive'
    else:
        print('here 2')
        x = value[0]
        y = value[1]
        color = value[2]

    return [x, y, color]





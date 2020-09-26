import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import web_layout.navbar as navbar
import web_layout.data_table as data_table
from dash_react_table import DashReactTable
import pandas as pd
from dash.dependencies import Input, Output
import repository as repo

# create dash
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    navbar.navbar(),
    html.Br(),

    html.Div(children=[
        # table of data
        dbc.Row(children=[
            html.Div([
                data_table.get_table_of_data(),
            ], className='col-9 '),

            dbc.Col([
                dbc.Table(

                )
            ])
        ], className='col-9'),

        # active vs inactive worker

        dbc.Row(children=[
            html.Div(children=[
                html.H4('Active vs Inactive workers'),
            ], className='col-6'),

            html.Div(children=[
                html.H4('Female workers vs Male workers'),
            ], className='col-6'),
        ], style={'text-align': 'center'}, className='mt-4')

    ], className='m-4')
])


# for data_table.get_table_of_data()
@app.callback(
    Output('table-of-data', 'data'),
    [Input('table-of-data', "page_current"),
     Input('table-of-data', "page_size"),
     Input('table-of-data', 'sort_by')])
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = data_table.df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False,
        )
    else:
        # No sort is applied
        dff = data_table.df

    return dff.iloc[
           page_current * page_size:(page_current + 1) * page_size
           ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)

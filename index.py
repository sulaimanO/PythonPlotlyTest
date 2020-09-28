import dash
import dash_html_components as html
import dash_core_components as core
import dash_bootstrap_components as dbc
import web_layout.navbar as navbar
import web_layout.data_table as data_table
from dash.dependencies import Input, Output
import web_layout.CardView as card
import services.general_data as gt
import web_layout.pieChart as pie
import plotly.express as px

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
            ], className='col-7'),

            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        card.card_with_title_and_number('number of people', gt.general_numbers()[0]),
                    ], className='col-3'),
                    dbc.Col([card.card_with_title_and_number('number of countries', gt.general_numbers()[1])],
                            className='col-3'),
                    dbc.Col([card.card_with_title_and_number('number of females', gt.general_numbers()[2])],
                            className='col-3'),
                    dbc.Col([card.card_with_title_and_number('number of males', gt.general_numbers()[3])],
                            className='col-3'),
                ])
            ])
        ]),

        # active vs inactive worker

        dbc.Row(children=[
            html.Div(children=[
                html.H4('General visualization about the data'),
                pie.active_inactive_dropdown_list()
            ], className='col-6'),

            html.Div(children=[
                html.H4('Female workers vs Male workers'),
            ], className='col-6'),
        ], className='mt-4')

    ], className='m-4')
])


# for active and inactive piechart
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(my_dropdown):
    dff = pie.df

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)



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

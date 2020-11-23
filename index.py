import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import services.general_data as gt
import web_layout.BarChart as bar_chart
import web_layout.CardView as card
import web_layout.data_table as data_table
import web_layout.navbar as navbar
import web_layout.pieChart as pie
import web_layout.options_dropdow_list as opt_dropdown
import dash_core_components as dcc

# create dash
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    navbar.navbar(),
    html.Br(),

    html.Div(children=[
        html.Div([
            dbc.Row([
                card.card_with_title_and_number('number of people', gt.general_numbers()[0]),
                card.card_with_title_and_number('number of countries', gt.general_numbers()[1]),
                card.card_with_title_and_number('number of females', gt.general_numbers()[2]),
                card.card_with_title_and_number('number of males', gt.general_numbers()[3]),

                html.Div([
                    data_table.get_table_of_data(),
                ], className='col-6 ml-3'),

            ])
        ], className="col-12"),

        dbc.Row(children=[
            html.Div(children=[
                pie.all_data_pie(options=opt_dropdown.select_options(job_title=False, country=False),
                                 label="Gender, Work Active, State")
            ], className='col-6 card'),
        ], className="ml-2"),

        dbc.Row(children=[
            html.Div(children=[
                html.H4('Comparing data by'),

                bar_chart.comparing_data_by_dropdown_list(
                    first_dropdown_list_id="type_of_data_dropdown_list",
                    second_dropdown_list_id="type_of_data_dropdown_list2",
                    graph_id="type_of_data_graph",
                    options_list_1=opt_dropdown.select_options(),
                    options_list_2=opt_dropdown.select_options(country=False, job_title=False),
                    slider_id="slider_comparing"),


            ], className='col-12'),

        ], className='mt-4'),
    ], className='m-2')
])


# Comparing data by
@app.callback(
    Output(component_id='type_of_data_graph', component_property='figure'),
    [Input(component_id='type_of_data_dropdown_list', component_property='value'),
     Input(component_id='type_of_data_dropdown_list2', component_property='value'),
     Input(component_id='slider_comparing', component_property='value')]
)
def compare_data_by_bar_chart(type_of_data, type_of_data_2, slider_value):
    print(slider_value)
    return bar_chart.comparing_data_by_figure(type_of_data, type_of_data_2, slider_value)


# General visualization about the data
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(my_dropdown):
    dff = pie.df

    return px.pie(
        data_frame=dff,
        names=my_dropdown,
        hole=.3,
    )


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

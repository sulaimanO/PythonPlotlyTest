# https://plotly.com/python/bar-charts/
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import services.general_data as gt

df = gt.get_table_of_all_data()[0]


# Comparing data by gender
def comparing_data_by_dropdown_list(first_dropdown_list_id, graph_id, options_list_1, options_list_2,
                                    slider_id=None, slider_range=None, second_dropdown_list_id=None):
    col_length = "col-12"
    if slider_id and second_dropdown_list_id:
        col_length = "col-4"
    elif slider_id or second_dropdown_list_id:
        col_length = "col-6"

    first_dropdown_list = html.Div([
        html.Label(['select from the list below']),
        dcc.Dropdown(
            id=first_dropdown_list_id,
            options=options_list_1,
            value='State',
            multi=False,
            clearable=False,
            style={"width": "100%"}
        ),
    ], className=col_length)

    graph = html.Div([dcc.Graph(id=graph_id)])

    slider_div = html.Div([])
    total_records = gt.general_numbers()[0]

    if slider_id is not None:
        if slider_range is not None:
            total_records = slider_range

        slider_div = html.Div([
            html.Label(['Number of records to compare']),
            dcc.Slider(
                id=slider_id,
                min=1,
                max=total_records,
                step=0.5,
                value=10,
                marks={
                    1: '1',
                    total_records // 2: str(total_records // 2),
                    total_records: str(total_records)
                }
            ),
            html.Div(id='slider-output-container')
        ], className="col-4 mt-auto")

    if second_dropdown_list_id is not None:
        second_dropdown_list = html.Div([
            html.Label(['select from the list below']),
            dcc.Dropdown(
                id=second_dropdown_list_id,
                options=options_list_2,
                value='gender',
                multi=False,
                clearable=False,
                style={"width": "100%"}
            ),
        ], className=col_length)

        return html.Div([
            dbc.Row([
                first_dropdown_list,
                second_dropdown_list,
                slider_div
            ]),
            graph
        ])

    return html.Div([
        first_dropdown_list,
        slider_div,
        graph
    ])


# TODO: Refactor this
def comparing_data_by_figure(x, compare_by, number_of_data=None):
    y_count = gt.general_numbers()[0]

    if number_of_data is not None:
        dff = df.head(int(number_of_data))
        print(dff)
        return px.bar(
            data_frame=dff,
            x=x,
            color=compare_by,
            barmode='group',
            range_y=[0, number_of_data],
        )

    return px.bar(
        data_frame=df,
        x=x,
        color=compare_by,
        barmode='group',
        range_y=[0, y_count],
    )

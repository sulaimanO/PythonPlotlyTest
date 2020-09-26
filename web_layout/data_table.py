import dash_table
import Resources as r
import pandas as pd
import services.general_data as gt
import dash_html_components as html

df = gt.get_data_without_id_and_index()

def get_table_of_data():
    gt.general_numbers()
    table = dash_table.DataTable(
                id='table-of-data',
                columns=[
                    {"name": i, "id": i} for i in df.columns
                ],
                style_header={
                  'text-align': 'center',
                  'font-weight': 'bold',
                  'font-size': 'large',
                },
                style_data={
                  'text-align': 'center'
                },
                page_current=0,
                page_size=r.PAGE_SIZE,
                page_action='custom',

                sort_action='custom',
                sort_mode='single',
                sort_by=[],
            )

    return table
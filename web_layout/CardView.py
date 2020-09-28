import dash_html_components as html
import dash_bootstrap_components as dbc

def card_with_title_and_number(title, number):
    card = dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H6(title, className="text-xs text-primary text-uppercase mb-1"),
                    html.H4(number, className="mb-0 font-weight-bold text-gray-800"),
                ])
            ], className='no-gutters align-items-center'),
        ])
    ], className='border-left-primary py-2')

    return card
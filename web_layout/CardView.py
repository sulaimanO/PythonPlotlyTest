import dash_html_components as html
import dash_bootstrap_components as dbc


def card_with_title_and_number(title, number):
    card = html.Div([
        html.H6(number, className="mb-0 font-weight-bold text-gray-800"),
        html.P(title, className="text-xs text-primary text-capitalize"),
    ], style={"border-radius": "5px",
              "background-color": "#f9f9f9",
              "width": "13rem",
              "height": "6rem",
              "box-shadow": "2px 2px 2px lightgrey",
              "margin": "10px",
              "padding": "15px"
              })

    return card

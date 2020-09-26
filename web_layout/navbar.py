import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import Resources as r


def navbar():
    nav = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=r.get_logo(), height="30px")),
                        dbc.Col(dbc.NavbarBrand(r.navbar_title, className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            # dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
        ],
        color="dark",
        dark=True,
    )

    return nav

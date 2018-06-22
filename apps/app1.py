import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3(children='Menu', className="w3-bar-item"),
    dcc.Link(children='Go to App 2', href='/my/app2', className="w3-bar-item w3-button"),
    html.Div(id='app-1-link-value'),
    dcc.Link(children='Link1', href='/my3/app3', className="w3-bar-item w3-button"),
    dcc.Link(children='Link2', href='#', className="w3-bar-item w3-button"),
    dcc.Link(children='Link3', href='#', className="w3-bar-item w3-button"),
], className="w3-sidebar w3-light-grey w3-bar-block", style={'width':'18%'})


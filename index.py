import flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from apps import app1, app2, app3


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

import ssl
from pymongo import MongoClient
mongo_uri = "mongodb+srv://nfbadmin:thornypowerpack@cluster0-v612w.mongodb.net/test"
conn = MongoClient(mongo_uri, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = conn.mysample

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/my/app1':
         return app1.layout
    elif pathname == '/my/app2':
         return app2.layout
    elif pathname == '/my3/app3':
         return app3.layout
    else:
        rec = db.student.find()[0]
        return rec['name']

@server.route("/")
def MyDashApp():
    return app.index()

if __name__ == '__main__':
    server.run(debug=True, port=5000)

from dash import Dash

static_folder = 'static'

app = Dash(__name__, static_folder=static_folder)
app.config.suppress_callback_exceptions = True

server = app.server

stylesheets = ['bWLwgP.css','mycss.css','w3.css']


for stylesheet in stylesheets:
    app.css.append_css({"external_url": "/{}/{}".format(static_folder, stylesheet)})


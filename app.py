<<<<<<< HEAD
from dash import Dash

static_folder = 'static'

app = Dash(__name__, static_folder=static_folder)
app.config.suppress_callback_exceptions = True

server = app.server

stylesheets = ['bWLwgP.css','mycss.css','w3.css']


for stylesheet in stylesheets:
    app.css.append_css({"external_url": "/{}/{}".format(static_folder, stylesheet)})

=======
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M:%S %p")

    return """
    <h1>Hello World</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
>>>>>>> 336828064e288f6b0352750becc95f547e0f8f14

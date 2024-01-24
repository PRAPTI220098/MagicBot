import flask
from threading import Thread

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "<b>hello</b>"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


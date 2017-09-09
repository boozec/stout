from flask import Flask, render_template
from .config import config

app = Flask(__name__)

@app.route("/")
def hello():
    with open(config['path'], 'rb') as fout:
        try:
            lines = fout.readlines()
        except Exception as e:
            lines = ''

        if lines is not None:
            lista = [x.strip() for i, x in enumerate(lines) if i > 0]
        else:
            lista = []

    try:
        return render_template("index.html", list_todo = lista, len_todo = len(lista))
    except Exception as e:
        return 'errore: %s' % e

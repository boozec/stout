from flask import Flask, render_template
from .classes import r

app = Flask(__name__)

@app.route("/")
def hello():
    lista = r.zrange('todo', 0, -1)
    try:
        return render_template("index.html", list_todo = lista, len_todo = len(lista))
    except Exception as e:
        return 'errore: %s' % e

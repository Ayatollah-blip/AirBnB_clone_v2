#!/usr/bin/python3
""" module doc"""

from flask import Flask, render_template
from flask_sqlalhemy import SQLAlchemy
from models import storage
app = Flask(__name__)


@app.route("/states_list/", strict_slashes=False)
def cities_by_States:
    """ retrieve state from storage (either file data or database)  """
    states = sorted(list(storage.all("State").values(), key=lambda x: x.name))
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown:
    """ close app  """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

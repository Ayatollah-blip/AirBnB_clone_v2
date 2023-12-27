#!/usr/bin/python3
""" module doc"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """ def doc"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ def doc"""
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """ def doc """
    return "C " + text.replace('_',' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

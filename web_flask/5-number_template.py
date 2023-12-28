#!/usr/bin/python3
""" module doc"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """ def doc"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ def doc"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ def doc """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_rout(text='is cool'):
    """ function that writes python +
    text and if text is null python is cool """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_rout(n):
    """ return if number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>',  strict_slashes=False)
def number_template_rout(n):
    """ return HTML if n is number"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

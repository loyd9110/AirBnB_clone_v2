#!/usr/bin/python3
"""A flask script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """function to return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """function to display "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index_c_is_fun(text):
    """func displays C is fun"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def index_python(text="is cool"):
    """func that displays python and value of text"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def index_number(n):
    """Return a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def index_num_template(n):
    """Display HTML page only if n is an integer"""
    return render_template("5-number.html", p=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def index_odd_or_even(n):
    """Display html page with variables"""
    if n % 2 == 0:
        is_odd_or_even = "even"
    else:
        is_odd_or_even = "odd"

    return render_template("6-number_odd_or_even.html", p=n, m=is_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

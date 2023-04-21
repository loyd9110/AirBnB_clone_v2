#!/usr/bin/python3
"""A flask script that starts a Flask web application"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

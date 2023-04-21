#!/usr/bin/python3
"""A flask script to display "Hello HBNB!" """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Method to return hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

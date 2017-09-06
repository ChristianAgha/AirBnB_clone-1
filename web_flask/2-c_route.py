#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    prints Hello HBNB!
    """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """
    prints HBNB!
    """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    Displays "C " followed by value of text
    """
    text = "C " + text.replace('_', ' ')
    return(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

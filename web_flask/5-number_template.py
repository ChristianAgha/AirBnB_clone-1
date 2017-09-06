#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask, abort, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py(text='is cool'):
    """
    Displays "Python " followed by value of text
    """
    py_text = "Python " + text.replace('_', ' ')
    return(py_text)


@app.route('/number/<n>', strict_slashes=False)
def display_n(n):
    """
    Displays n is a number" only if n is an integer
    """
    try:
        return("{} is a number".format(int(n)))
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def display_template(n):
    """
    display an HTML page only if n is an int
    """
    try:
        number = int(n)
        return render_template('5-number.html', number=number)
    except:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

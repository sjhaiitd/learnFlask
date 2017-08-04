# First Flask Project
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/flask")
def index():
    return "<html><head><title>Hi there!</title></head><body>Hello World!</body></html>", 200


@app.route("/jinja")
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

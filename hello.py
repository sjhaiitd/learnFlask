# First Flask Project
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/flask")
def index():
    return "Hello Nginx World 05Aug2017"

if __name__ == '__main__':
    app.run(debug=True)

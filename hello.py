# First Flask Project
from flask import Flask

app = Flask(__name__)


@app.route("/flask")
def index():
    return "Hello Flask Nginx"


if __name__ == '__main__':
    app.run(debug=True)

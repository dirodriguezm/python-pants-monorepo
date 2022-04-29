from lib1.greet import Greeter
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    g = Greeter()
    return g.greet("Larva")

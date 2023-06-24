from lib1.greet import Greeter
from flask import Flask
from confluent_kafka import Consumer

app = Flask(__name__)


@app.route("/")
def main():
    g = Greeter()
    return g.greet("Larva")

from app2 import __version__
from app2.app import app, Greeter
from unittest import mock


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    with mock.patch.object(Greeter, "greet") as greet:
        with app.test_client() as client:
            client.get("/")
            greet.assert_called_with("Larva")

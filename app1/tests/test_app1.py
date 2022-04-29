from app1 import __version__
from app1.app import main, Greeter
from unittest import mock


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    with mock.patch.object(Greeter, "greet") as greet:
        main()
        greet.assert_called_with("Larva")

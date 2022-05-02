from lib1 import __version__
from lib1.greet import Greeter


def test_version():
    assert __version__ == "0.1.3"


def test_greet():
    g = Greeter()
    res = g.greet("name")
    assert "Hello, name" in res

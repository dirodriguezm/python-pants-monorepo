from lib1.greet import Greeter


def test_greet():
    g = Greeter()
    res = g.greet("name")
    assert "Hello, name" in res

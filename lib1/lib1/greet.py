from colors import green


class Greeter:
    def greet(self, name):
        text = f"Hello, {name}."
        print(green(text))
        return text

    def goodbye(self, name):
        text = f"Goodbye, {name}."
        print(green(text))
        return text

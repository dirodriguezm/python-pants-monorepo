from colors import green


class Greeter:
    def greet(self, name):
        text = green(f"Hello, {name}")
        print(text)
        return text

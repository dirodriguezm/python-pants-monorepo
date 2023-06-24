from lib1.greet import Greeter
from lib2.main import main as lib2_main


def main():
    g = Greeter()
    g.greet("Larva")
    lib2_main()


if __name__ == "__main__":
    main()

from classes import *

def main():
    x = Analisador()
    x.analisar("Python")

    print()

    x.analisar(3)

    print()

    x.analisar([1, 2, 3, 4, 5])

    print()

    x.analisar(3.8)

if __name__ == "__main__":
    main()

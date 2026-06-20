from retangulo import Retangulo
from rich import inspect

def main():
    r = Retangulo()

    r.base = 12
    r.altura = 33
    print(r.medidas)

    print()

    r.medidas = (9, 3)
    print(r.medidas)


    inspect (r, private=True, methods=True)

if __name__ == '__main__':
    main()

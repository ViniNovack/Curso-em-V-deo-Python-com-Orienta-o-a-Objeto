from quadrado import Quadrado
from circulo import Circulo

def main():
    q1 = Quadrado(12)
    print(q1.perimetro())
    print(q1.area())

    print('=-'*30)

    c1 = Circulo(2)
    print(c1.perimetro())
    print(c1.area())

if __name__ == '__main__':
    main()

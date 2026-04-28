from bebida_quente import Bebida_Quente
from cafe import Cafe
from cha import Cha
from leite import Leite

def main():
    bebida1 = Cafe()
    print(bebida1.preparar())

    print('=-'*30)

    bebida2 = Cha()
    print(bebida2.preparar())

    print('=-'*30)

    bebida3 = Leite()
    print(bebida3.preparar())

if __name__ == '__main__':
    main()

from guerreiro import Guerreiro
from mago import Mago

def main():
    p1 = Guerreiro('Kratos', 2000)
    p2 = Mago('Merlin', 3000)

    print('\n','=-'*30)

    print(p1.atacar(p2, 1000))
    print(p2.atacar(p1, 1000))

    print('=-'*30)

    print(p1.ver_vida())
    print(p2.ver_vida())

    print('=-'*30)

    print(p1.curar())
    print(p2.curar())

    print('=-'*30,'\n')

if __name__ == '__main__':
    main()

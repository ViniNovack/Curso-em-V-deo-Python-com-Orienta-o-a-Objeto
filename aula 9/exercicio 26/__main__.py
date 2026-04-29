from horista import Horista
from mensalista import Mensalista

def main():
    f1 = Horista('Paulo', 12, 200)
    print(f'{f1.calc_sal()}', end='')
    print(f'{f1.analisar_sal()}')

    print('=-'*38)

    f2 = Mensalista('Amanda', 9500)
    print(f'{f2.calc_sal()}', end='')
    print(f'{f2.analisar_sal()}')

if __name__ == '__main__':
    main()

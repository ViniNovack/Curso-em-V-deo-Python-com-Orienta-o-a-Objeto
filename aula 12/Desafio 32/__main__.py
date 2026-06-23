from ContaBancaria import ContaBancaria
from rich import inspect

def main():
    print('Criando a conta...')
    cc = ContaBancaria(299792458, 'Gustavo', 1000, 'senha123')

    print('Realizando depósito')
    cc.depositar(500, 'senha123')

    print('Realizando saque')
    cc.sacar(200, 'senha123')

    cc.nome = 'Vinícius'

    inspect(cc, private=True, methods=True)
    
if __name__ == '__main__':
    main()

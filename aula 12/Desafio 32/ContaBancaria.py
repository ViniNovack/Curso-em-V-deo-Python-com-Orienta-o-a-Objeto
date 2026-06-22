import hashlib

class ContaBancaria:
    def __init__(self, id, nome, senha='', saldo=0):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if senha == '':
            senha = str(input("Digite uma senha para sua protação: "))
        self.__senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def __str__(self, senha=''):
        if senha == '':
            senha = str(input("Digite uma senha para sua protação: "))
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        else:
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        if senha == self.__senha:
            return f'Acesso CONCEDIDO, Bem vindo {self._titular}\nEstado atual da conta: {self.__dict__}'
        else:
            return 'Acesso NEGADO!'

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor=''):
        if valor == '':
            print('Não é permitido trocar o valor da conta, apenas fazer saques e depositos')
        else:
            print('Não é permitido trocar o valor da conta, apenas fazer saques e depositos')

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def saldo(self, nome):
        if isinstance(nome, int):
            print('Um nome não pode ter apenas números\nNome novo INVALIDO')
        else:
            self._titular = nome
            print(f'O nome {nome} foi registrado com sucesso!')

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            print('A troca foi invalida, só se podem números no id')

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo +=valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self._id}')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            x = str(input('Você não tem todo esse dinheiro, mas você pode sacar todo o valor da comta? (Y/N)\n'))
            if (x.lower()).strip() == 'y':
                self.sacar(self.__saldo)
                print(f'Saque de R${self.__saldo:.2f} autorizado na conta {self._id}')
        else:
            self.__saldo -=valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self._id}')

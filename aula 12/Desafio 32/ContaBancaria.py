class ContaBancaria:
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'Conta {self.id} criada com sucesso. __saldo atual de R${self.__saldo:.2f}')

    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo +=valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            x = str(input('Você não tem todo esse dinheiro, mas você pode sacar todo o valor da comta? (Y/N)\n'))
            if (x.lower()).strip() == 'y':
                self.sacar(self.__saldo)
                print(f'Saque de R${self.__saldo:.2f} autorizado na conta {self.id}')
        else:
            self.__saldo -=valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}')

    def __str__(self):
        # return f'A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo.'
        return f'Estado atual da conta: {self.__dict__}'             # "__dict__" ele tem a função de mostrar as variaveis com seus respectivos valores da função mâe
    
    def depositar(self, valor):
        self.saldo +=valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            x = str(input('Você não tem todo esse dinheiro, mas você pode sacar todo o valor da comta? (Y/N)\n'))
            if (x.lower()).strip() == 'y':
                self.sacar(self.saldo)
                print(f'Saque de R${self.saldo:.2f} autorizado na conta {self.id}')
        else:
            self.saldo -=valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')

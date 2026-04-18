class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo.'
    
    def depositar(self, valor):
        self.saldo +=valor
        print(f'Depósito de R${valor:.2f}')

    def sacar(self, valor):
        self -=valor







c1 = ContaBancaria(122, 'Gustavo', 3000)
print(c1)

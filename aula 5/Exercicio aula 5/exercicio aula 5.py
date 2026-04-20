from rich.traceback import install
install()

class ContaBancaria:
    """
    Parte basica de um sistema de banco
    """
    def __init__(self, id, name, saldo=0):
        self.id = id
        self.nome = name
        self.saldo = saldo
        
    def __str__(self):  
        return (f'Conta {self.id} criada com sucesso.\n'
               f'Saldo atual R${self.saldo:.2f}')
    
    def depositar(self, valor=0):
        self.saldo +=valor
        print(f'Saldo atual ficou: R${self.saldo:.2f}')
    
    def sacar(self, valor=0):
        if valor > self.saldo:
            print('Saque NÃO ALTORIZADO')
        else:
            self.saldo -=valor
            print(f'Sua conta atual ficou: R${self.saldo:.2f}')

c = ContaBancaria(33867, 'Vinícius', 10_000)
print(c)
c.depositar()
c.sacar()

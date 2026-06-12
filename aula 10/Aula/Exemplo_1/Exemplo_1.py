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

"""
    Existem três tipos de visibilidade para atributos em linguagem POO:
    > public +
    > protected #
    > private -

    public(+): Ela esta disponivel para todo o projeto
    protected(#): Ela esta disponivel para suas classes filhas
    private(-): Ela esta disponivel para a propria classe, mesmo as filhas não tem acesso

    ---- O PYTHON NÃO CONSIDERA NADA DISSO!("Liberdade com responsabilidade")
    Em python:
    > (+) atrib1
    > (#) _atrib2
    > (-) __atrib3
    Apesar delas estarem referenciadas como publics, protecteds e privates elas ainda podem ser alteradas, mas CONVENCIONALMENTE não são.(Mas podem!)
    
    !!!!!!!!!!! Essas mudanças e a ideia de poder mudar é possivel somente em python em outras linguagens como java, por exemplo, isso NÃO É POSSIVEL !!!!!!!!!!!!!!!
"""

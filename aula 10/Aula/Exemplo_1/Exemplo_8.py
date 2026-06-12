class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id # Público(+)
        self._titular = nome # Protegido(#)
        self.__saldo = saldo # Privado(-)
        print(f'Conta {self.id} criada com sucesso. __saldo atual de R${self.__saldo:.2f}')

    def __str__(self):
        # return f'A conta {self.id} de {self._titular} tem R${self.__saldo:.2f} de __saldo.'
        return f'Estado atual da conta: {self.__dict__}'             # "__dict__" ele tem a função de mostrar as variaveis com seus respectivos valores da função mâe
    
    def depositar(self, valor):
        valor = abs(valor)             # O "abs" transforma uma valor no seu valor absoluto(Exemplo: -2 -> 2 / -77 -> 77)
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

"""
    ENCAPSULAMENTO
    - Visa manter a integridade do sistema, protegendo o estado interno do objeto contra interferência externa não regulamentada

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

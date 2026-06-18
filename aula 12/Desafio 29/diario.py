class Diario():
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha
    
    @property
    def escrever(self):
        return self.__segredos
    
    @escrever.setter
    def escrever(self, texto):
        x = isinstance(texto, str)
        if x == True:
            self.__segredos.append(texto)
        else:
            print(f'!!O dado [{texto}] é INVALIDO!!')

    def ler(self, senha):
        if senha == self.__senha:
            print('DIÁRIO LIBERADO!')
            for c in self.__segredos:
                print('- ', c)
        else:
            print('!!ESCREVA A SENHA CORRETA PARA LER!!')

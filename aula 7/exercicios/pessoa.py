class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome:str = nome
        self.idade:int = idade

    def aniversario(self):
        self.idade +=1

    def acabou(self, nome):
        return f'O turno acabou para {nome}'

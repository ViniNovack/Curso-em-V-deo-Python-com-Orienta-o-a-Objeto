class Gafanhoto:
    def __init__(self):
        self.nome = ''
        self.idade = 0
    
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f'{self.nome} têm {self.idade} anos.'

g1 = Gafanhoto()
g1.nome = 'Carlos'
g1.idade = 88
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Marina'
g2.idade = 33
print(g2.mensagem())

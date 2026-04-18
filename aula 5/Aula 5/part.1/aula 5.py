class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, n='', i=0):
        self.nome = n
        self.idade = i
    
    def aniversario(self):
        self.idade +=1
    
    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

g1 = Gafanhoto('Maria', 17)
print(g1)

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
# print(g3.mensagem())

# print(g1.__doc__)  # Dunder Attribute
# print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

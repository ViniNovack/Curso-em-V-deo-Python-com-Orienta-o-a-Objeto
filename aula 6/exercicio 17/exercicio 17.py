class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def etiqueta(self):
        print('PRODUTO'.center(30))
        print(f'{self.nome}'.center(30))
        print('-'*30)
        print(f'{self.preço}\n'.center(30))


c1 = Produto('Notebook', 20_000)
c1.etiqueta()

c2 = Produto('Notebool DELL', 22_500)
c2.etiqueta()

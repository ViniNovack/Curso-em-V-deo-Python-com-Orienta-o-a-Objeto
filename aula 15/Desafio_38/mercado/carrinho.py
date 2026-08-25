from mercado.produto import *

class Carrinho():
    def __init__(self):
        self.produtos = []

    def __add__(self, outro):
        if isinstance(outro, Produto):
            self.produtos.append(outro)

        elif isinstance(outro, Carrinho):
            pass

        else:
            raise TypeError("Só é possivel adicionar carrinho e produto")

        return Carrinho()

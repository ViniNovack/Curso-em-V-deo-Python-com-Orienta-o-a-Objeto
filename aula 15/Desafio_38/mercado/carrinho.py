from mercado.produto import *

class Carrinho():
    def __init__(self):
        self.produtos = []

    @property
    def total(self):
        soma = 0
        for p in self.produtos:
            soma +=p.preco
        return soma

    def __add__(self, outro):
        if isinstance(outro, Produto):
            self.produtos.append(outro)

        elif isinstance(outro, Carrinho):
            for x in outro.produtos:
                self.produtos.append(x)

        else:
            raise TypeError("Só é possivel adicionar carrinho e produto")

        return Carrinho()

    def __str__(self):
        texto_formatado = "\n".join(self.produtos)
        return texto_formatado

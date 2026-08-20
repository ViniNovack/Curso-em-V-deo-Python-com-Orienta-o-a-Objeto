from abc import ABC
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Pagamento(ABC):
    def __init__(self):
        self.__valor = None

    @property
    def fvalor(self):
        val = self.__valor
        return locale.currency(val, grouping=True)

    @property
    def valor(self):
        pass

    @valor.setter
    def valor(self, valor):
        pass


# DUCK TYPING
def finalizar_compra(clas, valor):
    try:
        clas.finalizar_compra(valor)
    except:
        print(f"A forma de pagamento {clas} não foi encontrada.")

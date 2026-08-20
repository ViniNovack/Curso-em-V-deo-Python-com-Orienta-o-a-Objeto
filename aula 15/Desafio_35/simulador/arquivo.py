from abc import ABC

class Arquivo(ABC):
    def __init__(self, nome, tamanho, extensao):  #baites /6
        self.nome = nome
        self.tamanho = tamanho
        self._extensao = extensao

    @property
    def nome_completo(self):
        return f"'{self.nome}{self.extensao}'({self.tamanho/1_000_000}MB)"

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        raise ValueError("Não se pode alterar a extensao")


# DUCK TYPING
def abrir_arquivo(objeto):
    try:
        objeto.abrir_arquivo()
    except:
        print(f"Não foi possivel abrir o objeto {objeto}")

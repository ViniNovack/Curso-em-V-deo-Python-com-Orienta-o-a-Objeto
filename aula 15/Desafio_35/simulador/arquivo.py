from abc import ABC

class Arquivo(ABC):
    def __init__(self, nome, tamanho, extensao):  #baites
        self.nome = nome
        self.tamanho = tamanho
        self._extensao = extensao

    @property
    def nome_completo(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        raise ValueError("Não se pode alterar a extensao")

    def abrir_arquivo(objeto):
        try:
            objeto.abrir_arquivo()
        except:
            return f"Não foi possivel abrir o objeto {objeto}"

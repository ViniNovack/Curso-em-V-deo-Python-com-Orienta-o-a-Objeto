from simulador.arquivo import *

class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, ".pdf")

    def abrir_arquivo(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, ".doc")

    def abrir_arquivo(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")

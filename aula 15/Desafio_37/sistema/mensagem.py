from abc import ABC

class Mensagem(ABC):
    def __init__(self, mensagem):
        self._mensagem = mensagem
        self._tipo = "Aviso"
        self._icone = "💬"

        self.definir()
        
    @property
    def mensagem(self):
        return self._mensagem
    
    @mensagem.setter
    def mensagem(self, valor):
        raise TypeError("Não se pode alterar o valor")
    
    def definir_mensagem(self, valor):
        self._mensagem = valor


    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        raise TypeError("Não se pode alterar o valor")
    
    def definir_tipo(self, valor):
        self._tipo = valor
    

    @property
    def icone(self):
        return self._icone
    
    @icone.setter
    def icone(self, valor):
        raise TypeError("Não se pode alterar o valor")
    
    def definir_icone(self, valor):
        self._icone = valor

    def definir(self, tipo, icone):
        self.definir_tipo(tipo)
        self.definir_icone(icone)

    def mostrar(self):
        print(f"{self.icone} {self.tipo} {self.icone}\n"
              f"[{self.mensagem}]")

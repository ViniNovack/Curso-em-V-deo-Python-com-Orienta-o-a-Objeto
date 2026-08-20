from sistema.mensagem import *

class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
    
    def definir(self):
        super().definir("ERRO", "❌")

class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
    
    def definir(self):
        super().definir("ALERTA", "⚠️")

from simul_pag.pagamento import *

class Boleto(Pagamento):
    def __init__(self):
        super().__init__()
    
    def finalizar_compra(self, valor):
        self._definir_valor(valor)
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto")

class Credito(Pagamento):
    def __init__(self):
        super().__init__()
    
    def finalizar_compra(self, valor):
        self._definir_valor(valor)
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Crédito")

class Pix(Pagamento):
    def __init__(self):
        super().__init__()
    
    def finalizar_compra(self, valor):
        self._definir_valor(valor)
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Pix")

class Debito(Pagamento):
    def __init__(self):
        super().__init__()
    
    def finalizar_compra(self, valor):
        self._definir_valor(valor)
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Debito")

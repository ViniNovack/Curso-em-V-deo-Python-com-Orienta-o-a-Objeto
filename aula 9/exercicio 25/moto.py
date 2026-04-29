from transporte import Transporte

class Moto(Transporte):
    fator:int = 0.5

    def __init__(self, distancia:int):
        super().__init__('Moto', distancia)

    def calc_frete(self) -> int:
        f = (Moto.fator) * (self.distancia)
        return f
    
    def nome(self) -> str:
        return super().nome()

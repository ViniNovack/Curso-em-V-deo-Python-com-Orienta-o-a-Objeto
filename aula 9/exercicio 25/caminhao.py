from transporte import Transporte

class Caminhao(Transporte):
    fator:int = 1.20

    def __init__(self, distancia:int):
        super().__init__('Caminhão', distancia)
    
    def calc_frete(self):
        if self.distancia >= 50.00:
            f = (self.distancia) * (Caminhao.fator)
            return f
        else:
            return 'O caminhão tem uma distancia mínima de 50km'

    def nome(self) -> str:
        return super().nome()

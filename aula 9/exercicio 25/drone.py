from transporte import Transporte

class Drone(Transporte):
    fator:int = 9.50

    def __init__(self, distancia:int):
        super().__init__('Drone', distancia)
    
    def calc_frete(self):
        if self.distancia <= 10.00:
            f = (Drone.fator) * (self.distancia)
            return f
        else:
            return 'O drone vai no maximo até uma distancia maxima de 10km'

    def nome(self) -> str:
        return super().nome()

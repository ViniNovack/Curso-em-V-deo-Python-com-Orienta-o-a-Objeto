from transporte import Transporte

class Drone(Transporte):
    fator:int = 9.50

    def __init__(self, distancia):
        super().__init__('Drone', distancia)
    
    def calc_frete(self) -> int:
        f = (Drone.fator) * (self.distancia)
        return f

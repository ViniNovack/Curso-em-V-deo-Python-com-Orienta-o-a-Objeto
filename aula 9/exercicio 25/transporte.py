from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, transporte:str, distancia:int):
        self.transporte = transporte
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass

from abc import ABC, abstractmethod

class Poligonos(ABC):
    def __init__(self, lado):
        self.lado = lado
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

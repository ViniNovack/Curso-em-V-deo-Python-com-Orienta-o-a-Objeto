from poligonos import Poligonos

class Quadrado(Poligonos):
    def lad(self, lado):
        super().__init__(lado)
    
    def perimetro(self) -> str:
        p = self.lado * 4
        return f'O perimetro do quadrado é {p:.2f}'
    
    def area(self) -> str:
        a = self.lado ** 2
        return f'A area do quadrado é {a:.2f}'

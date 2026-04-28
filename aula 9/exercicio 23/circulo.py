from poligonos import Poligonos

class Circulo(Poligonos):
    def raio(self, raio):
        super().__init__(raio)
    
    def perimetro(self) -> str:
        p = 2 * 3.14 * self.lado
        return f'O perimetro do circulo é {p:.2f}'
    
    def area(self) -> str:
        a = 3.14 * (self.lado ** 2)
        return f'A area do circulo é {a:.2f}'

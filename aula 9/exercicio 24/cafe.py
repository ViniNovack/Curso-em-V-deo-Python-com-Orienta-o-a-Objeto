from bebida_quente import Bebida_Quente

class Cafe(Bebida_Quente):
    def __init__(self):
        super().__init__('Café')

    def misturar(self) -> str:
        return 'Passando água pressurizada pelo pó de café moído.'

    def servir(self) -> str:
        return 'Servindo em xícara pequena.'

    def preparar(self):
        return super().preparar(super().ferver_agua(), self.misturar(), self.servir())

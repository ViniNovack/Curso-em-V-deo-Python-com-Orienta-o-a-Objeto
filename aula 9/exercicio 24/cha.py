from bebida_quente import Bebida_Quente

class Cha(Bebida_Quente):
    def __init__(self):
        super().__init__('Chá')

    def misturar(self) -> str:
        return 'Mergulhando o sachê de ervas na água.'

    def servir(self) -> str:
        return 'Servindo na caneca de porcelana com limão'

    def preparar(self):
        return super().preparar(super().ferver_agua(), self.misturar(), self.servir())

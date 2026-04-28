from bebida_quente import Bebida_Quente

class Leite(Bebida_Quente):
    def __init__(self):
        super().__init__('Leite')
    
    def misturar(self) -> str:
        return 'Passando vapor pressurizado pelo bico do leite.'

    def servir(self) -> str:
        return 'Servindo na caneca grande, já com chá.'

    def preparar(self):
        return super().preparar(super().ferver_agua(), self.misturar(), self.servir())

from funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, nome:str, valor_horas:int, qtd_horas:int):
        super().__init__(nome)
        self.valor_horas = valor_horas
        self.qtd_horas = qtd_horas

    def calc_sal(self) -> str:
        s = self.valor_horas * self.qtd_horas
        return super().calc_sal(s)
    
    def analisar_sal(self) -> str:
        return super().analisar_sal()

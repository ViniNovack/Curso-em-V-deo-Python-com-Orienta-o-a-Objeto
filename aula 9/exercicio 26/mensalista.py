from funcionario import Funcionario

class Mensalista(Funcionario):
    def __init__(self, nome:str, salario_bruto:int):
        super().__init__(nome)
        self.salario_bruto = salario_bruto
    
    def calc_sal(self) -> str:
        return super().calc_sal(self.salario_bruto)

    def analisar_sal(self) -> str:
        return super().analisar_sal()

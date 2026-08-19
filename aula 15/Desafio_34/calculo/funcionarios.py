from calculo.funcionario import *

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        super().calcular_bonus(15)

class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        super().calcular_bonus(8)

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        super().calcular_bonus(10)

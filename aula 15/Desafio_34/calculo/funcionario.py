from abc import ABC

class Funcionario(ABC):
    def __init__(self, nome, salario:int|float):
        self.nome = nome
        self._salario = None
        self.bonus = None

        self.salario = salario
        self.calcular_bonus()

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("Tipo de valor invalido, apenas 'int' ou 'float'")

        if self._salario is not None and valor < self._salario:
            raise ValueError("Não se pode diminuir salario")

        self._salario = valor
        self.calcular_bonus()

    def __str__(self):
        return f"{self.nome} ganha R${self.salario} e por ser {self.__class__.__name__} o bônus será de R${self.bonus}"

    def calcular_bonus(self, bonuss):
        self.bonus = self.salario * (bonuss/100)
        return self.bonus

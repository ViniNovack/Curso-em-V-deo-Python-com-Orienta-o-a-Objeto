from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:int|float = 1_621):
        self.nome = nome
        self.__salario = None
        self.bonus = None

        self.salario = salario
        self.calcular_bonus()

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("Tipo de valor invalido, apenas 'int' ou 'float'")

        if self.__salario is not None and valor < self.__salario:
            raise ValueError("Não se pode diminuir salario")

        self.__salario = valor
        self.calcular_bonus()

    def __str__(self):
        return f"{self.nome} ganha R${self.salario} e por ser {self.__class__.__name__} o bônus será de R${self.bonus}"

    @abstractmethod
    def calcular_bonus(self, bonuss):
        self.bonus = self.salario * (bonuss/100)
        return self.bonus

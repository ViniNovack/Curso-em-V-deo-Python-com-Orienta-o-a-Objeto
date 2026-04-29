from abc import ABC, abstractmethod

class Funcionario(ABC):
    sal_min:int = 1612
    inss:int = 0.925

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calc_sal(self, salario:int) -> str:
        return f'O salário de/a {self.nome} é de {salario}.'

    @abstractmethod
    def analisar_sal(self, analize:int) -> str:
        return f'Ele corresponde a {analize} salários mínimos.'

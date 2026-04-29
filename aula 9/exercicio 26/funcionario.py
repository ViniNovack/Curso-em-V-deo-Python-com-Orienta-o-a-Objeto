from abc import ABC, abstractmethod

class Funcionario(ABC):
    sal_min:int = 1612
    inss:int = 0.925

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calc_sal(self, salario:int) -> str:
        s = salario * Funcionario.inss
        self.salario = s
        return (f'{'ANÁLISE DE SALÁRIO':^74}\n') + (f'O salário de/a {self.nome} é de {s:.2f}. ')

    @abstractmethod
    def analisar_sal(self) -> str:
        a = self.salario / Funcionario.sal_min
        return f'Ele corresponde a {a:.2f} salários mínimos.'

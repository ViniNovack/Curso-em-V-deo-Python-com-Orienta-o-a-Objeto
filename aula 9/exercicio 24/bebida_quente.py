from abc import ABC, abstractmethod

class Bebida_Quente(ABC):
    def __init__(self, preparo):
        self.preparo:str = preparo

    def preparar(self, passo_um:str, passo_dois:str, passo_tres:str):
        return ('--- Iniciando o Preparo ---\n'
                f'1. {passo_um}\n'
                f'2. {passo_dois}\n'
                f'3. {passo_tres}\n'
                '--- Bebida Pronta ---')

    def ferver_agua(self):
        return f'Fervendo água para o {self.preparo} a 100 graus Celsius.'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

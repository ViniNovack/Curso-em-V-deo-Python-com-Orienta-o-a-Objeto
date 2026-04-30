from abc import ABC, abstractmethod
from random import randrange

class Personagens(ABC):
    def __init__(self, nome:str, vida:int):
        self.nome = nome
        self.vida_atual = vida
        self.vida_max = vida
    
    @abstractmethod
    def atacar(self, alvo, força):
        f = randrange(1, 7)
        self.ataq = força * (0.166 * f)
        alvo.vida_atual -=self.ataq
    
    @abstractmethod
    def curar(self):
        vv = self.vida_atual
        self.v = self.vida_max / 2
        f = randrange(1, 7)
        self.v *=(0.166 * f)
        vv +=self.v
        if vv > self.vida_max:
            self.v = self.vida_max - self.vida_atual
            self.vida_atual = self.vida_max
        else:
            self.vida_atual +=self.v
    
    def ver_vida(self):
        return f'A vida do {self.nome} é {self.vida_atual:.2f}'

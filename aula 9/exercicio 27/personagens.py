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
        ataq = força * (0.166 * f)
        alvo.vida -=ataq
    
    @abstractmethod
    def curar(self):
        vv = self.vida_atual
        v = self.vida_max / 2
        f = randrange(1, 7)
        v *=(0.166 * f)
        vv +=v
        if vv > self.vida:
            self.vida_atual = self.vida_max
        else:
            self.vida_atual +=v

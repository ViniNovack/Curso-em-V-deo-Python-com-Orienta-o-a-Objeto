from abc import ABC, abstractmethod
from random import randrange

class Personagem(ABC):
    def __init__(self, nome:str, vida:int):
        self.nome = nome
        self.vida = vida
    
    @abstractmethod
    def atacar(self, alvo, força):
        pass

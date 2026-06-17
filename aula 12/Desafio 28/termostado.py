from abc import ABC, abstractmethod

class Termostato(ABC):
    def __init__(self):
        self.__temperatura = 24
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if (16 <= valor <= 30):
            self.__temperatura == valor
        else:
            return f'O termostato já atingiu o valor mínimo/máximo: {self.__temperatura}ºC'

    @abstractmethod
    def mostrar(self):
        return f'A temperatura atual é {self.__temperatura}'
    
    def aumentar_temp(self):
        pass

    def baixar_temp(self):
        pass

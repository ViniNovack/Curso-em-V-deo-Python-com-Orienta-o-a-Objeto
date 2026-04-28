from abc import ABC, abstractmethod

class Bebida_Quente(ABC):
    def __init__(self, preparo):
        self.preparo = preparo

    def preparar(self, passo_um, passo_dois, passo_três):
        return (f'--- Iniciando o Preparo ---'
                f'')
               
        
    
    def ferver_agua(self):
        return f'Fervendo água para o {self.praparo} a 100 graus Celsius.'
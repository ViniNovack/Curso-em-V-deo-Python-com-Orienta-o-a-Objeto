from abc import ABC, abstractmethod
from datetime import datetime

def verf_idade(date_ano):
    ano = datetime.now().year
    if 0 < (ano - date_ano) <= 125:
        return True
    else:
        return False

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int, idade=None):
        self._nome = nome
        
        if verf_idade(nasc):
            self._nascimento = nasc
        else:
            raise ValueError('Essa data é INVALIDA!')
        
        if idade == None:
            ano = datetime.now().year
            self.__idade = ano - nasc
        else:
            raise ValueError('A idade não pode ser alterada apenas a data de nascimento')

#   ------------------------------------- NOME -------------------------------------
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self._nome = nome
        else:
            raise ValueError('O nome não pode ser um valor')
    
#   ------------------------------------- NASCIMENTO -------------------------------------
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, nasc):
        if isinstance(nasc, int):
            if verf_idade(nasc):
                self._nascimento = nasc
                self.__idade = (datetime.now().year) - nasc
            else:
                raise ValueError('Essa data é INVALIDA!')
        else:
            raise ValueError('A data de nacimento precisa ser um número inteiro')
    
#   ------------------------------------- IDADE -------------------------------------
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade
        else:
            raise ValueError('A idade precisa ser um valor inteiro')
#   -----------------------------------------------------------------------------------

    @abstractmethod
    def mostrar(self, ob):
        print(ob.__dict__)

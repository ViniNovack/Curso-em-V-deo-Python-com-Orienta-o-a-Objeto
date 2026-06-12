"""
    Acesso aos Dados
    Existem duas maneiras de permitir o acesso aos dados encapsulados:
    -> Uso de getters e setters
    -> Uso de decorador @property

    > Getters: É um método acessor utilizado para obter o valor de um atributo que foi encapsulado ou protegido dentro de uma classe
    > Setters: São métodos especiais criados para permitir a alteração segura de valores de atributos que estão encapsulados

    
"""

class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected(#)
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        Criando Atributo Validável         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @property
    def nota(self):            # getter
        return self._nota
    
    @nota.setter
    def nota(self, valor):     #setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')

    @nota.deleter
    def nota(self):
        pass

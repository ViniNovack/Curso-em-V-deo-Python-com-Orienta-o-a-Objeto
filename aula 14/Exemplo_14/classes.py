from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod      # Caso ele não identifique nem um tipo estabelesido ele executa esse
    def analisar(self, valor):
        print(f"Não foi possível analizar o valor {valor}")

    @analisar.register
    def _(self, valor:int):
        print(f"{valor} é um número INTEIRO")

    @analisar.register
    def _(self, valor:str):
        print(f"{valor} é uma cadeia de caracteres")

    @analisar.register
    def _(self, valor:tuple|list|dict):
        print(f"{valor} é uma coleção de dados")

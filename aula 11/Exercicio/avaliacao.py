class Avaliacao:
    def __init__(self, nome:str, disciplina:str, nota:int=0):
        self.nome = nome
        self.diciplina = disciplina
        self._nota = nota
    
    @property
    def nota(self):          # Getter
        return self._nota
    
    @nota.setter
    def nota(self, valor:int):
        n = abs(valor)
        if (0 <= n <= 10):
            self._nota = n
        else:
            print(f'Desculpa, mas o valor [{valor}] é invalido!')

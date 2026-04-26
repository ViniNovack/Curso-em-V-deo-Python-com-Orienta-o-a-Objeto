from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self) -> str:
        return f'O professor {self.nome} está em aula.'
    
    def acabou(self, nome):
        return super().acabou(nome)

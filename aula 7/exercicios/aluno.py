from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def matricula(self) -> str:
        return f'O aluno {self.nome} fez a sua matricula.'
    
    def acabou(self, nome) -> str:
        return super().acabou(nome)

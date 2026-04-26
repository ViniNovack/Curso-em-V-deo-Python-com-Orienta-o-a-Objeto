from rich import print, inspect

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome:str = nome
        self.idade:int = idade

    def aniversario(self):
        self.idade +=1

    def acabou(self, nome):
        return f'O tunirno acabou para {nome}'

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def matricula(self) -> str:
        return f'O aluno {self.nome} fez a sua matricula.'
    
    def acabou(self):
        super().acabou(self.nome)
    
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self) -> str:
        return f'O professor {self.nome} esté em aula.'
    
class funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self) -> str:
        return f'O/A funcionario/a {self.nome} bateu o ponto'

a1 = Aluno('Vinínicius', 17, 'Computação', 'T01')
print(a1.matricula())
a1.aniversario()
inspect(a1)
print(a1.acabou())

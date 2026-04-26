from rich import print, inspect
from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def verif():
    a1 = Aluno('Vinícius', 17, 'Computação', 'T01')
    print(a1.matricula())
    a1.aniversario()
    inspect(a1)
    print(a1.acabou('Vinícius'))

    print('=-'*30)

    p1 = Professor('Peter', 30, 'Matemática', 'Doutor')
    print(p1.dar_aula())
    p1.aniversario()
    inspect(p1)
    print(p1.acabou('Peter'))

    print('=-'*30)

    f1 = Funcionario('João', 39, 'Diretor', 'Diretoria')
    print(f1.bater_ponto())
    f1.aniversario()
    inspect(f1)
    print(f1.acabou('João'))

if __name__ == '__main__':
    verif()
else:
    print('FIM')

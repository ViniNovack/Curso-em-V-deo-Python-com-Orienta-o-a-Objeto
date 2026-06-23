from rich import inspect
from aluno import Aluno

def main():
    a1 = Aluno('Maria', 2000)

    a1.add_curso('moda')
    a1.curso = 'MODA'
    a1.nascimento = 2010

    inspect(a1, private=True, methods=True)

if __name__ == '__main__':
    main()

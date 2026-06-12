from avaliacao import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao('Vinícius', 'Matemática')
    av1.nota = 10
    print(f'O aluno {av1.nome} na materia de {av1.diciplina} ficou com {av1.nota}')
    inspect(av1, private=True)

if __name__ == '__main__':
    main()

from diario import Diario

def main():
    d = Diario('senha123')
    d.escrever = 'Primeira mensagem'
    d.escrever = 'Você é uma pessoa simpática'
    d.escrever = 'Você gosta de Python'

    d.ler('senha123')

if __name__ == '__main__':
    main()

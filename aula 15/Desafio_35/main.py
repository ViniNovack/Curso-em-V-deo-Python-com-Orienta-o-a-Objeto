from simulador.arquivos import *

def main():
    a1 = DOC("prova", 250_000)
    a2 = PDF("contrato", 1_300_000)

    abrir_arquivo(a2)
    print(a2.nome_completo)

if __name__ == "__main__":
    main()

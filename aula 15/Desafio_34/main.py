from calculo.funcionarios import *
from calculo.funcionario import *

def main():
    f = Desenvolvedor("Pedro", 1_800)
    f.salario = 1_000
    print(f)

if __name__ == "__main__":
    main()

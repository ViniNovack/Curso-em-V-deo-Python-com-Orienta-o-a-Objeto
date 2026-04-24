class Funcionario:
    # Atributos de Classe !!!!!!!!!!!!!!!!!!!!!!
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self) -> str:                      # -> str !!!!!!!!!!!!!!!
        return f'🤝 Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.\n'

# Funcionario.empresa = 'Novack'                          # Os atributos de Classe podem ser alterados por fora depois !!!!!!!!!!!!!!!!

c1 = Funcionario('Vinícius', 'Junior', 'Desenvolvedor')
print(c1)

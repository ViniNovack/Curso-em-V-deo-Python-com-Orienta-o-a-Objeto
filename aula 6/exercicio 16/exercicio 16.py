class Funcionario:
    def __init__(self, nome, setor, cargo, empresa='Curso em Vídeo'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def __str__(self):
        return f'🤝 Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}.\n'


c1 = Funcionario('Vinícius', 'Junior', 'Desenvolvedor')
print(c1)

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.L = []

    def add_favorito(self, jogo):
        (self.L).append(jogo)

    def ficha(self):
        LL = sorted(self.L)
        print(f'Jogador {self.nick}'.center(30))
        print('-'*30)
        print(f'Nome real. {self.nick}'.center(10))
        print('Jogos favoritos: '.center(10))
        for c in LL:
            print(f'👾 {c}'.center(10))
        print('_'*30)
        print()

j1 = Gamer('Vinícius', 'ViniMarvel7769')
j1.add_favorito('Marvel Rivals')
j1.add_favorito('Batman arkan')
j1.add_favorito("Assasino s'creed")
j1.ficha()

j2 = Gamer('Lucas', 'Peter011')
j2.add_favorito('Paladins')
j2.add_favorito('Fortnite')
j2.ficha()

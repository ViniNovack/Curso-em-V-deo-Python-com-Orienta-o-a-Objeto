from rich import print
from rich.panel import Panel

class Controle:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 6

    def __init__(self, canal = 1, volume = 1, estado=False):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.estado_atual:bool = estado
    
    def ligado(self):
        self.estado_atual = True
        print('TV'.center(30))
        print('-'*30)
        return True

    def canais(self):
        if self.estado_atual == True:
            conteudo = ''
            for c in range(Controle.canal_min, (Controle.canal_max + 1)):
                if c == self.canal_atual:
                    conteudo += (f'[yellow on yellow] {c} [/]')
                else:
                    conteudo += (f' {c} ')
            return conteudo
        elif self.estado_atual == False:
            return('🚫 A TV está desligada')
    
    def volume(self):
        if self.estado_atual == True:
            valores = ''
            for c in range(Controle.volume_min, (Controle.volume_max + 1)):
                if self.volume_atual == c:
                    for i in range(Controle.volume_min, (c + 1)):
                        valores +=(f'[blue on blue] [/]')
                    for f in range(c, Controle.volume_max):
                        valores +=(f'[black on black] [/]')
                    break      
            return valores

    def troca(self, s):
        if s == '>':
            self.canal_atual +=1
            if self.canal_atual > Controle.canal_max:
                self.canal_atual = Controle.canal_min
        elif s == '<':
            self.canal_atual -=1
            if self.canal_atual < Controle.canal_min:
                self.canal_atual = Controle.canal_max
        elif s == '+':
            self.volume_atual +=1
            if self.volume_atual > Controle.volume_max:
                self.volume_atual = Controle.volume_max
        elif s == '-':
            self.volume_atual -=1
            if self.volume_atual < Controle.volume_min:
                self.volume_atual = Controle.volume_min

c1 = Controle()
c1.ligado()
print(c1.canais())
print(c1.volume())
while True:
    x = input(str('Digite < ou >: \n'))
    if x == '0':
        print('FIM')
        break
    else:
        c1.troca(x)
        print(c1.canais())
        print(c1.volume())

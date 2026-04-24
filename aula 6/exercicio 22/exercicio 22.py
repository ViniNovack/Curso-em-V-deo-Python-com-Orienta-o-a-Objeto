from rich import print
from rich.panel import Panel
import os

class Controle:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 6

    def __init__(self, canal = 1, volume = 1, lig=0, estado=False):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.estado_atual:bool = estado
        self.lig:int = lig
    
    def ligado(self, l='x'):
        if l == '@':
            self.lig +=1
            if self.lig > 1:
                self.lig = 0
            
            if self.lig == 0:
                self.estado_atual = False
                print('🚫 A TV está desligada')
                return False
            elif self.lig == 1:
                self.estado_atual = True
                print('TV'.center(30))
                print('-'*30)
                return True
        elif l == 'x':
            if self.lig == 0:
                self.estado_atual = False
                print('🚫 A TV está desligada')
                return False
            elif self.lig == 1:
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
            return ''
    
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
        else:
            return ''

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
l = False
while True:
    x = input(str('Digite: @ para ligar ou desligar '
                  '< ou > para canais / + ou - para volume \n'))
    if x == '0':
        os.system('cls')
        print('FIM')
        break
    elif x == '@' or x == '>' or x =='<' or x == '+' or x == '-':
        if x == '@':
            os.system('cls')
            l = c1.ligado(x)
            print(c1.canais())
            print(c1.volume())
        else:
            if l == True:
                os.system('cls')
                c1.troca(x)
                c1.ligado()
                print(c1.canais())
                print(c1.volume())
            else:
                os.system('cls')
                c1.ligado()
    else:
        os.system('cls')
        c1.ligado()

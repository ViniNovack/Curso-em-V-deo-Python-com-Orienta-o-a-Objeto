class Caneta:
    def __init__(self, cor):
        if cor == 'branco':
            self.cor = '\033[30m'
        elif cor == 'vermelho':
            self.cor = '\033[31m'
        elif cor == 'verde':
            self.cor = '\033[32m'
        elif cor == 'amarelo':
            self.cor = '\033[33m'
        elif cor == 'azul':
            self.cor = '\033[34m'
        elif cor == 'magenta':
            self.cor = '\033[35m'
        elif cor == 'ciano':
            self.cor = '\033[36m'
        elif cor == 'cinza':
            self.cor = '\033[37m'
        
        self.tampa = False
    
    def destampar(self):
        self.tampa = True
    
    def escrever(self, texto):
        # LIMPAR
        limpar = '\033[m'

        if self.tampa == False:
            print('A caneta está tampada, NÃO TEM COMO ESCREVER!!!')
        else:
            print(f'{self.cor}{texto}{limpar}')

c1 = Caneta('verde')
c2 = Caneta('azul')
c3 = Caneta('amarelo')

c1.destampar()
##############
c3.destampar()

c1.escrever('Olá, mundo')
c2.escrever('Olá, mundo')
c3.escrever('Olá, mundo')

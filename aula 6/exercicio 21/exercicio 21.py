class Caneta:
    def __init__(self, cor='azul'):
        match cor.lower().strip():                                       # match/case !!!!!!!!!!!!!!!!!!!!!!!!!!!
            case 'branco':
                self.cor = '\033[30m'
            case 'vermelho':
                self.cor = '\033[31m'
            case 'verde':
                self.cor = '\033[32m'
            case 'amarelo':
                self.cor = '\033[33m'
            case 'azul':
                self.cor = '\033[34m'
            case 'magenta':
                self.cor = '\033[35m'
            case 'ciano':
                self.cor = '\033[36m'
            case _:                                                      # caso a variavel não se encaixe em nem uma categoria !!!!!!!!!!!!!!!!!!!!
                self.cor = '\033[1m'
        
        self.tampa = False
    
    def destampar(self):
        self.tampa = True
    
    def tampar(self):
        self.tampa = False
    
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

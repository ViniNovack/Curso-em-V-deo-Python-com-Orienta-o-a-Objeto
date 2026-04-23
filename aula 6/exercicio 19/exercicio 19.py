class Livro:
    def __init__(self, titulo, paginas, posição=1):
        self.titulo = titulo
        self.paginas = paginas
        self.posição = posição

    def avançar(self, s=1):
        print(f'Você acabou de abrir o livro "{self.titulo}" que tem {self.paginas} páginas no total.')
        if s == 1:
            print('Você agora está na página 1')
        else:
            v = 0
            print(f'Atualmete você esta na pagina {self.posição}')
            for c in range((self.posição), (s + 1)):
                print(f'Pág{c} > ',end='')
                v +=1
                self.posição +=1
                if self.posição > self.paginas:
                    print(f'Você avançõu {v} páginas e agora esta na pagina 20')
                    print(f'VOCÊ NÃO PODE AVANÇAR MAIS, POIS CHEGOU AO FIM DE {self.titulo}')
                    break
                else:
                    continue
            
            if self.posição > self.paginas:
                print(f'Você avançou {v} páginas e agora está na página 20')
            else:
                print(f'Você avançou {v} páginas e agora está na página {self.posição}')


c1 = Livro('DUNA', 20)
c1.avançar()
c1.avançar(5)
c1.avançar(10)
c1.avançar(100)

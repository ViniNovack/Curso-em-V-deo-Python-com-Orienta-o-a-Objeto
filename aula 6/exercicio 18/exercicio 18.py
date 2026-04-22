class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    def __str__(self):
        q = 0.4 * (self.quant)
        comp = q * 82.4
        div = comp / self.quant
        
        return (f'Analisando {self.titulo} com {self.quant} convidados\n'
                 'Cada participante comerá 0.4kg e cada Kg custa R$82.40\n'
                f'Recomendo comprar {q}Kg de carne\n'
                f'O custo total será de R${comp:.2f}\n'
                f'Cada pessoa pagará R${div:.2f} para participar')
    

c1 = Churrasco('Churras com os PARSA', 15)
print(c1)

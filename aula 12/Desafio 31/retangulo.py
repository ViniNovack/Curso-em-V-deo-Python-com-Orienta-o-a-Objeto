class Retangulo():
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        self._area = None
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError('Não se pode inseir valores negativos ou 0')
        else:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError('Não se pode inserir valores negativos ou 0')
        else:
            self._altura = valor

    @property
    def area(self):
        return (self._base * self._altura)

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, medidas):
        if (medidas[0] <= 0) or (medidas[1] <= 0):
            raise ValueError('Não se pode inserir valores negativos ou 0')
        else:
            self._base = medidas[0]
            self._altura = medidas[1]

class Retangulo():
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError('Não se pode inseir valores negativos ou 0')
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('O valor da base deve ser um número!')
        else:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError('Não se pode inserir valores negativos ou 0')
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('O valor da altura deve ser número!')
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = (self._base * self._altura)
        return self._area
    
    @area.setter
    def area(self):
        raise PermissionError('Área não pode ser configurada, por essa forma!')

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, medidas:tuple):
        if (medidas[0] <= 0) or (medidas[1] <= 0):
            raise ValueError('Não se pode inserir valores negativos ou 0')
        if len(medidas) != 2:
            raise SyntaxError('Só se pode tuple com dois valores!')
        if not isinstance(medidas, tuple):
            raise TypeError('As medidas devem ser informadas dentro de uma tupla')
        else:
            self._base = medidas[0]
            self._altura = medidas[1]

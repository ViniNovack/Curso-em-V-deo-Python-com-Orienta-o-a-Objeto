class Termostato():
    def __init__(self):
        self.__temperatura = 24
    
    def __str__(self) -> str:
        return f'O termostato foi LIGADO'
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if (16 <= valor <= 30) and (valor % 1 in (0, 0.5)):
            self.__temperatura = valor

        elif (valor > 30) and (valor % 1 in (0, 0.5)):
            self.__temperatura = 30

        elif (valor < 16) and (valor % 1 in (0, 0.5)):
            self.__temperatura = 16

        else:
            print(f'O termostato já atingil o seu valor mínimo/maximo de {self.temperatura}ºC')

    def aumentar_temp(self, valor=1):
        self.temperatura +=(0.5 * valor)

    def baixar_temp(self, valor=1):
        self.temperatura -=(0.5 * valor)

    def mostrar_temp(self):
        print(f'A temperatura atual é {self.temperatura}')

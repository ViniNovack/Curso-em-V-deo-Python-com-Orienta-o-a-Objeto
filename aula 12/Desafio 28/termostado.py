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
        if valor % 0.5 != 0:
            raise ValueError(f'A Temperatura {valor} é INVALIDA!')

        if (16 <= valor <= 30):
            self.__temperatura = valor

        elif (valor > 30):
            self.__temperatura = 30

        elif (valor < 16):
            self.__temperatura = 16

        else:
            print(f'O valor {self.temperatura} ultrabaça os valores minímo/maximo do termostato.')
    
    @property
    def ftemperatura(self):
        return f'{self.__temperatura}{chr(176)}C'

    def aumentar_temp(self, valor=1):
        self.temperatura +=(0.5 * valor)

    def baixar_temp(self, valor=1):
        self.temperatura -=(0.5 * valor)

    def mostrar_temp(self):
        print(f'A temperatura atual é {self.ftemperatura}')

from personagens import Personagens

class Mago(Personagens):
    def __init__(self, nome:str, vida:int):
        super().__init__(nome, vida)
    
    def atacar(self, alvo:Personagens, força:int):
        super().atacar(alvo, força)
        return f'O Mago {self.nome} fez um ataque de {self.ataq:.2f} no {alvo.nome}'
    
    def curar(self):
        super().curar()
        return f'O Mago {self.nome} se curor em {self.v:.2f}. Agora ele tem {self.vida_atual:.2f}.'

    def ver_vida(self):
        return super().ver_vida()

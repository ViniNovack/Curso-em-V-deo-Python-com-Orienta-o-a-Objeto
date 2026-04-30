from personagens import Personagens

class Guerreiro(Personagens):
    def __init__(self, nome:str, vida:int):
        super().__init__(nome, vida)
    
    def atacar(self, alvo:Personagens, força:int):
        super().atacar(alvo, força)
        return f'O Guerreiro {self.nome} atacou com um chute giratorio o {alvo.nome}. Dando {self.ataq:.2f} de dano.'
    
    def curar(self):
        super().curar()
        return f'O Guerreiro {self.nome}, se curou em {self.v:.2f}. Agora ele está com {self.vida_atual:.2f} de vida.'

    def ver_vida(self):
        return super().ver_vida()

import hashlib

class Credencial():
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        if len(senha) > 0:
            converçao_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            self.__hash = converçao_hash
        else:
            raise ValueError('Senha inválida')

    def validar(self, senha_suj):
        converção_hash_suj = hashlib.sha256(senha_suj.encode('utf-8')).hexdigest()
        if converção_hash_suj == self.senha:
            return ('Senha está CORRETA!\n' + str(True))
        else:
            return ('Senha não BATE!\n' + str(False))

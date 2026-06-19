import hashlib

class Credencial():
    def __init__(self):
        self.__senha = ''

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        converçao_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        self.__senha = converçao_hash

    def validar(self, senha_suj):
        converção_hash_suj = hashlib.sha256(senha_suj.encode('utf-8')).hexdigest()
        if converção_hash_suj == self.senha:
            return ('Senha está CORRETA!\n' + str(True))
        else:
            return ('Senha não BATE!\n' + str(False))

import hashlib

class ContaBancaria:
    def __init__(self, id:int, nome:str, saldo:float=0, senha:str=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if senha == None:
            senha = self.pede_senha()
        self.__senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def __str__(self, senha:str=None):
        if senha == None:
            senha = self.pede_senha()
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        if senha == self.__senha:
            return f'Acesso CONCEDIDO, Bem vindo {self._titular}\nEstado atual da conta: {self.__dict__}'
        else:
            return 'Acesso NEGADO!'

    def pede_senha(self) -> str:
        while True:
            senha = str(input("Senha: ")).strip()
            if len(senha) >=6:
                break
            else:
                continue
        return senha
    
    def validar_senha(self, senha) -> bool:
        usuario = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        if usuario == self.senha:
            return True
        else:
            return False

#   ------------------------------------- SALDO ---------------------------------

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor=None):
        if valor == None:
            print('Não é permitido trocar o valor da conta, apenas fazer saques e depositos')
        else:
            print('Não é permitido trocar o valor da conta, apenas fazer saques e depositos')

#   ------------------------------------- TITULAR ---------------------------------

    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, nome):
        senha = self.pede_senha()
        if self.validar_senha(senha):
            if isinstance(nome, int):
                print('Um nome não pode ter apenas números\nNome novo INVALIDO')
            else:
                self._titular = nome
                print(f'O nome {nome} foi registrado com sucesso!')
        else:
            print("Senha não confere. Não posso alterar o nome")

#   ------------------------------------- ID ---------------------------------

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            print('A troca foi invalida, só se podem números no id')

#   -------------------------------- SENHA ---------------------------------------

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha:str=None):
        if senha == None:
            senha = str(input('Digite sua senha para sua proteção: '))
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        else:
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        if senha == self.__senha:
            print('Você está altorizado a trocar a sua senha!')
            senha = str(input('Digite a nova senha: '))
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            self.__senha = senha
        else:
            print('Senha errada, troca de senha INVALIDA!')

#   ------------------------------------------------------------------------------

    def depositar(self, valor, senha:str=None):
        if senha == None:
            senha = str(input('Digite sua senha: '))
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        else:
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        
        if senha == self.senha:
            valor = abs(valor)
            self.__saldo +=valor
            print(f'Depósito de R${valor:.2f} autorizado na conta {self._id}')
        else:
            print('Senha está invalida, transação CANCELADA!')

    def sacar(self, valor, senha:str=None):
        if senha == None:
            senha = str(input('Digite sua senha, para sua segurança: '))
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        else:
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        
        if senha == self.senha:
            valor = abs(valor)
            if valor > self.__saldo:
                x = str(input('Você não tem todo esse dinheiro, mas você pode sacar todo o valor da comta? (Y/N)\n'))
                if (x.lower()).strip() == 'y':
                    self.sacar(self.__saldo)
                    print(f'Saque de R${self.__saldo:.2f} autorizado na conta {self._id}')
            else:
                self.__saldo -=valor
                print(f'Saque de R${valor:.2f} autorizado na conta {self._id}')
        else:
            print('Senha incoreta, tranferencia INVALIDA!')

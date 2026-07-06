"""
import hashlib

def main():
    # 1. Cadastro: Simulando a senha que foi salva no banco de dados (em formato hash)
    senha_cadastrada = 'senha123'
    hash_banco_dados = hashlib.sha256(senha_cadastrada.encode('utf-8')).hexdigest()

    # 2. Login: O que o usuário digitou para tentar entrar
    tentativa_login = 'senha123'

    # 3. Correção: Geramos o hash do que foi digitado para comparar com o hash salvo
    hash_tentativa = hashlib.sha256(tentativa_login.encode('utf-8')).hexdigest()

    # Agora comparamos HASH com HASH
    if hash_tentativa == hash_banco_dados:
        print(True)   # A senha está correta!
    else:
        print(False)  # A senha está errada!

if __name__ == "__main__":
    main()
"""
import hashlib      # OU from hashlib import sha256
texto = "Gafanhoto"
cod = texto.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()

if __name__ == "__main__":
    print(hash)

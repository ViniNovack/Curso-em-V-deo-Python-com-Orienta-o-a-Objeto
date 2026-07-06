from hash_sha256_senha import Credencial

def main():
    c = Credencial()
    
    c.senha = 'senha123'
    print(c.validar('senha123'))
    
    print()

    print(c.validar('senha'))

if __name__ == '__main__':
    main()

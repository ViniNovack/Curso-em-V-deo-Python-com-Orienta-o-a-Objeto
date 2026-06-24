from termostado import Termostato

def main():
    # t = Termostato()
    # print(t)
    # print(t.mostrar_temp())

    # t.aumentar_temp()
    # t.mostrar_temp()

    # t.baixar_temp(2)
    # t.mostrar_temp()

    # t.temperatura = 20
    # t.mostrar_temp()

    # t.temperatura = 32
    # t.mostrar_temp()

    # t.temperatura = 14
    # t.mostrar_temp()

    # t.temperatura = 22.2
    # t.mostrar_temp()

#   ---------------------------- CORRIGINDO ----------------------------

    t = Termostato()
    print(t)
    try:
        t.temperatura = 22.2
    except Exception as e:                                 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(f'Houve um problema: {e}')
    
    print(f'A temperatura atual é de {t.temperatura}\n')

    print(f'A temperatura atual é de {t.ftemperatura}')

if __name__ == '__main__':
    main()

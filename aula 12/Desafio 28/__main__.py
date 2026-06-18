from termostado import Termostato

def main():
    t = Termostato()
    print(t)
    print(t.mostrar_temp())
    
    t.aumentar_temp()
    print(t.mostrar_temp())
    
    t.baixar_temp(2)
    print(t.mostrar_temp())

    t.temperatura = 20
    print(t.mostrar_temp())

    t.temperatura = 32
    print(t.mostrar_temp())

    t.temperatura = 14
    print(t.mostrar_temp())

if __name__ == '__main__':
    main()

from moto import Moto
from drone import Drone
from caminhao import Caminhao

def main():
    distancia = 10
    
    t1 = Moto(distancia)
    print(f'Frete de {t1.nome()} em {distancia}Km = {t1.calc_frete()}')

    print('=-'*30)

    t2 = Drone(distancia)
    print(f'Frete de {t2.nome()} em {distancia}km = {t2.calc_frete()}')

    print('=-'*30)

    t3 = Caminhao(distancia)
    print(f'Frete de {t3.nome()} em {distancia}km = {t3.calc_frete()}')

if __name__ == '__main__':
    main()

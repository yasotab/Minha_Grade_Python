#!/home/israel-salazar/Grade_Python/fundamentos_projetos/python3
from math import pi


def circulo(raio):
    print ('Área do circulo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)

#!/home/israel-salazar/Grade_Python/fundamentos_projetos/python3
from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo.")
        print("Sintaxe: {} <raio>".format(sys.argv[0]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print ('Área do círculo', area)

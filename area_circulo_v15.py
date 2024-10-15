#!/home/israel-salazar/Grade_Python/fundamentos_projetos/python3
from math import pi
import sys
import errno

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO+
              'O Raio deve ser um valor numérico'+TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print ('Área do círculo', area)

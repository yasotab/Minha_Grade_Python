#!/home/israel/Python/Grade_Python/estruturas_controle_projetos/python3
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if  len(resultado) == quantidade:
            break
    return resultado
        

if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequência
    for fib in fibonacci(20):
        print(fib)

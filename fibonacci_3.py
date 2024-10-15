#!/home/israel/Python/Grade_Python/estruturas_controle_projetos/python3
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')
        
    
if __name__ == '__main__':
    fibonacci(20000)

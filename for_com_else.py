PALAVRAS_PROIBIDAS = ('Futebol', 'Religião', 'Política')
textos = [
    'João gosta de Futebol e Política',
    'a praia foi divertida',
]


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto contém pelo menos uma palavra proibida', palavra)
            break

    else:
        print('Texto autorizado', texto)
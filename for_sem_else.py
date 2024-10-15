PALAVRAS_PROIBIDAS = ('Futebol', 'Religião', 'Política')
textos = [
    'João gosta de Futebol e Política',
    'a praia foi divertida',
]


for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto contém pelo menos uma palavra proibida', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado',)
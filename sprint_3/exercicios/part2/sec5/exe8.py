lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for p in lista:
    if p[::-1] == p:
        print(f'A palavra: {p} é um palíndromo')
    else:
        print(f'A palavra: {p} não é um palíndromo')
        
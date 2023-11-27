import random

random_list = random.sample(range(500), 50)


mediana = 0
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

lista_ordenada = sorted(random_list)
tamanho_lista = len(lista_ordenada)
if tamanho_lista % 2 == 0:
    mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
else:
    mediana = lista_ordenada[tamanho_lista // 2]

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')

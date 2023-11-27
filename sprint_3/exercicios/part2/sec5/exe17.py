def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_sublista = tamanho // 3

    if tamanho % 3 != 0:
        return "Não é possível dividir a lista em 3 partes iguais."


    parte1 = lista[:tamanho_sublista]
    parte2 = lista[tamanho_sublista: tamanho_sublista * 2]
    parte3 = lista[tamanho_sublista * 2:]

    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resultados = dividir_lista(lista)

print(resultados[0], resultados[1], resultados[2])

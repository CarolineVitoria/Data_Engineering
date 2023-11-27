def my_map(lista, funcao):
    return [funcao(elemento) for elemento in lista]


def potencia_de_2(numero):
    return numero ** 2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


resultado = my_map(lista, potencia_de_2)
print(resultado)

print(my_map(lista, potencia), "\n")
print(type(my_map(lista, potencia)))

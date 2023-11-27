lista = ["abc", "abc", "abc", "123", "abc", "123", "123"]


def retornaLista(lista):
    novaLista = list(set(lista))
    return novaLista


print(retornaLista(lista))

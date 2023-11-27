a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista = [] * len(a)

for n in a:
    if n % 2 != 0:
        lista.append(n)

print(lista)

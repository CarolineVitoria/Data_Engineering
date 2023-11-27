def soma(str):
    l = str.split(",")
    total = 0
    for numero in l:
        total += int(numero)

    return total


print(soma("1,3,4,6,10,76"))

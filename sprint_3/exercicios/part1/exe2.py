lista = [0] * 3
for i in range(3):
    lista[i] = int(input())
    if lista[i]%2 == 0 :
        print('Par: '+ str(lista[i]))
    else:
        print('Ímpar: '+ str(lista[i]))

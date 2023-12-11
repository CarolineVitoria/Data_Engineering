def ler_numeros(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return list(map(int, arquivo.readlines()))


numeros = ler_numeros('number.txt')

numeros_pares = filter(lambda x: x % 2 == 0, numeros)

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

cinco_maiores_pares = numeros_pares_ordenados[:5]

print(cinco_maiores_pares)

soma_cinco_maiores = sum(cinco_maiores_pares)
print(soma_cinco_maiores)

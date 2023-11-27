# Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média da coluna Gross.


def tratamentoDosRegistros(ator):
    novoNome = ator[0] + ator[1]
    ator[0] = novoNome.replace('"', "", 2)
    ator[0] = ator[0].replace(".", "", 1)
    for i in range(1, 6):
        c = i + 1
        ator[i] = ator[c]


gross_filmes = []
with open("actors.csv") as actors:
    for registro in actors:
        ator = registro.strip().split(",")
        if ator[0].find('"') != -1:
            tratamentoDosRegistros(ator)

        gross_filmes.append(ator[5])
gross_filmes.remove("Gross")


def impressaoResultado(media):
    f = open("etapa-2.txt", "w")
    f.write(f"Media de receita de bilheteria bruta dos principais filmes: {media}")
    f.close()
    print(f"Média de receita de bilheteria bruta dos principais filmes: {media}")


def mediaBilheteriaBruta(gross_filmes):
    soma = 0
    for n in gross_filmes:
        soma += float(n)

    media = soma / len(gross_filmes)
    impressaoResultado(media)


mediaBilheteriaBruta(gross_filmes)

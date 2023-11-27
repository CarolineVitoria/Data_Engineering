# Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna Avarage per Movie para fins de cálculo.


def tratamentoDosRegistros(ator):
    novoNome = ator[0] + ator[1]
    ator[0] = novoNome.replace('"', "", 2)
    ator[0] = ator[0].replace(".", "", 1)
    for i in range(1, 6):
        c = i + 1
        ator[i] = ator[c]


media_por_filmes = {}
with open("actors.csv") as actors:
    for registro in actors:
        ator = registro.strip().split(",")
        if ator[0].find('"') != -1:
            tratamentoDosRegistros(ator)

        media_por_filmes.update({ator[0]: ator[3]})
media_por_filmes.pop("Actor")

print(media_por_filmes)


def impressaoResposta(ator):
    f = open("etapa-3.txt", "w")
    f.write(
        f"ator/atriz com a maior media de receita de bilheteria bruta por filme: {ator}"
    )
    f.close()
    print(f"Média de receita de bilheteria bruta dos principais filmes: {ator}")


def maior_media(mediaFilme):
    soma = 0
    ator = ""
    for nome, media in mediaFilme.items():
        media = float(media)
        if media > soma:
            soma = media
            ator = nome
    return impressaoResposta(ator)


maior_media(media_por_filmes)

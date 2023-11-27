# Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.
def tratamentoDosRegistros(ator):
    novoNome = ator[0] + ator[1]
    ator[0] = novoNome.replace('"', "", 2)
    ator[0] = ator[0].replace(".", "", 1)
    for i in range(1, 6):
        c = i + 1
        ator[i] = ator[c]

total_filmes = {}
with open("actors.csv") as actors:
    for registro in actors:
        ator = registro.strip().split(",")
        if ator[0].find('"') != -1:
            tratamentoDosRegistros(ator)

        total_filmes.update({ator[0]: ator[2]})
total_filmes.pop("Actor")


def ator_mais_filmes(total_filmes):
    maiorQuantidade = 0
    ator_com_mais_filmes = ""

    for nome, filme in total_filmes.items():
        filme = int(filme)
        if int(filme) > maiorQuantidade:
            maiorQuantidade = filme
            ator_com_mais_filmes = nome
    f = open("etapa-1.txt", "w")
    f.write(
        "Ator com mais filmes: {}, Quantidade de filmes: {}".format(
            ator_com_mais_filmes, maiorQuantidade
        )
    )
    f.close()
    print(f'{ator_com_mais_filmes}, {maiorQuantidade}')

ator_mais_filmes(total_filmes)

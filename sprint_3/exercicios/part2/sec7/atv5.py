#Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.

#Ao escrever no arquivo, considere o padrão de saída <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha

def tratamentoDosRegistros(ator):
    novoNome = ator[0] + ator[1]
    ator[0] = novoNome.replace('"', "", 2)
    ator[0] = ator[0].replace(".", "", 1)
    for i in range(1, 6):
        c = i + 1
        ator[i] = ator[c]


bilheteria_filmes = {}
with open("actors.csv") as actors:
    for registro in actors:
        ator = registro.strip().split(",")
        if ator[0].find('"') != -1:
            tratamentoDosRegistros(ator)

        bilheteria_filmes.update({ator[0]: ator[1]})
bilheteria_filmes.pop("Actor")

def maior_bilheteria(bilheteria):
    count = 0
    for item in sorted(bilheteria_filmes, key= bilheteria_filmes.get, reverse=True):
        count+=1
        with open('etapa-5.txt', 'a+') as saida:
            print("{} - {}".format(item, bilheteria_filmes[item]), file=saida)
        print("{} - {}".format(item, bilheteria_filmes[item]))
maior_bilheteria(bilheteria_filmes)
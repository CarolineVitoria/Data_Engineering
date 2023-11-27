# A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do  filme.

#Ao escrever no arquivo, considere o padrão de saída <sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, adicionando um resultado a cada linha.

def tratamentoDosRegistros(ator):
    novoNome = ator[0] + ator[1]
    ator[0] = novoNome.replace('"', "", 2)
    ator[0] = ator[0].replace(".", "", 1)
    for i in range(1, 6):
        c = i + 1
        ator[i] = ator[c]

lista_filmes = []
with open("actors.csv") as actors:
    for registro in actors:
        ator = registro.strip().split(",")
        if ator[0].find('"') != -1:
            tratamentoDosRegistros(ator)

        lista_filmes.append(ator[4])
lista_filmes.remove("#1 Movie")
print(lista_filmes)

dict_filmes_repetidos = {}
for filme in lista_filmes:
    print(filme, lista_filmes.count(filme))
    quantidade_aparicoes = lista_filmes.count(filme)
    dict_filmes_repetidos.update({filme: quantidade_aparicoes})

print(dict_filmes_repetidos)
dict_ordenada = {}
valor_ordenado = []
count = 0
for item in sorted(dict_filmes_repetidos, key= dict_filmes_repetidos.get, reverse=True):
    count+=1
    
    with open('etapa-4.txt', 'a+') as saida:
        print("{} - o filme {} aparece {} vez(es) no dataset".format(
                count, item, dict_filmes_repetidos[item]), file=saida)
  
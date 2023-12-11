def processar_notas(estudante):
    nome, *notas = estudante.strip().split(',') 
    notas = list(map(int, notas)) 
    tres_maiores = sorted(notas, reverse=True)[:3] 
    media_tres_maiores = round(sum(tres_maiores) / 3, 2) 

    
    relatorio = f"Nome: {nome} Notas: {tres_maiores} Média: {media_tres_maiores}"
    return relatorio


with open('estudantes.csv', 'r') as arquivo:
    linhas = arquivo.readlines() 

relatorios = map(processar_notas, linhas)

for relatorio in sorted(relatorios):
    print(relatorio)

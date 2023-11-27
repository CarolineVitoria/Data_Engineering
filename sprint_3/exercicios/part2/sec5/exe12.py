import json

arq = open("person.json")
dados = json.load(arq)
arq.close
print(dados)

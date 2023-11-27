primeirosNomes = ["Joao", "Douglas", "Lucas", "José"]
sobreNomes = ["Soares", "Souza", "Silveira", "Pedreira"]
idades = [19, 28, 25, 31]

obj = list(enumerate(primeirosNomes))

for i in range(len(primeirosNomes)):
    print(
        "{} - {} {} está com {} anos".format(
            (obj[i][0]), (obj[i][1]), sobreNomes[i], idades[i]
        )
    )

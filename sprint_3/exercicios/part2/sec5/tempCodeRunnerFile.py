speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
valores = []
def a(speed):
    for chave, valor in speed.items():
        valores.append(valor)
    return list(set(valores))
a(speed)
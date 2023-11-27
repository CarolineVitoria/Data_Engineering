class Calculo:
    def soma(self, x, y):
        resultado = x + y
        return resultado

    def subtracao(self, x, y):
        resultado = x - y
        return resultado

x = 4
y = 5

calculo = Calculo()

resultado_soma = calculo.soma(x, y)
print(f"Somando: {x}+{y} = {resultado_soma}")

resultado_subtracao = calculo.subtracao(x, y)
print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")

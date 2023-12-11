def calcular_valor_maximo(operadores, operandos):

    def aplicar_operacao(op, operandos):
        x, y = operandos
        return eval(str(x) + op + str(y))
    
    resultados = map(lambda x: aplicar_operacao(*x), zip(operadores, operandos))
    
    max_v = max(resultados)
    return max_v

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado = calcular_valor_maximo(operadores, operandos)
print("Maior valor obtido:", resultado)

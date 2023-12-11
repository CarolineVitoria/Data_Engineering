from functools import reduce

def calcula_saldo(lancamentos): 
   
    calcular_lancamento = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]
    
    valores_a_somar = map(calcular_lancamento, lancamentos)
    
    saldo_final = reduce(lambda x, y: x + y, valores_a_somar, 0)
    
    return saldo_final

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

resultado = calcula_saldo(lancamentos)
print("O saldo final é:", resultado)

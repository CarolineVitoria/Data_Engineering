class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada

lista1= [3, 4, 2, 1, 5]
lista2=[9, 7, 6, 8]

crescente = Ordenadora(lista1)
crescente.ordenacaoCrescente()

decrescente = Ordenadora(lista2)
decrescente.ordenacaoDecrescente()

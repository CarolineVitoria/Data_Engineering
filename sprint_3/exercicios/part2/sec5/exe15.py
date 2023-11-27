class Lampada:
    def __init__(self, estado):
        self.ligada = estado  

    def liga(self):
        self.ligada = True  

    def desliga(self):
        self.ligada = False  

    def esta_ligada(self):
        return self.ligada 

lampada = Lampada(True) 

print("A lâmpada está ligada?" , lampada.esta_ligada()) 

lampada.desliga() 

print("A lâmpada está ligada?" , lampada.esta_ligada()) 

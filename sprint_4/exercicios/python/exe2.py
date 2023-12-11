def conta_vogais(texto:str)-> int:
    vogal = lambda char: char.lower() in ['a', 'e', 'i', 'o', 'u']
    
    vogais = filter(vogal, texto)
    
    total_vogais = len(list(vogais))
    
    return total_vogais


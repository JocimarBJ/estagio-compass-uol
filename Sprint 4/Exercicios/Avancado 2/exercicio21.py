def conta_vogais(texto:str)-> int:
    return len( list( filter( lambda x: x.lower() in 'aeiou', texto ) ) )

conta_vogais('texto')
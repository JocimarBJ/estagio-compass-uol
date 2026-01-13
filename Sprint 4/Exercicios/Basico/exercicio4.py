# Método Funcional
def remove_duplicados(lista): 
    return list(set(lista))
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(remove_duplicados(lista))
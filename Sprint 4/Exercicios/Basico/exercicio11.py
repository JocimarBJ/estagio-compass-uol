def dividir_lista(lista):
    # Validação: necessário tamanho da lista ser múltiplo de 3
    if len(lista) % 3 != 0:
        raise ValueError("A lista precisa ter tamanho múltiplo de 3")
    # Contando a quantidade de elementos e dividindo por 3
    n = len(lista)//3
    # Retorno: lista em 3 partes
    return lista[:n], lista[n:(2*n)], lista[(2*n):]
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista(lista)
print(parte1, parte2, parte3)
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

pessoas = list(zip(primeirosNomes, sobreNomes, idades))
for indice, (nome, sobrenome, idade) in enumerate(pessoas):
    print(f'{indice} - {nome} {sobrenome} está com {idade} anos')
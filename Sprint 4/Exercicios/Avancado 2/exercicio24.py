import csv
with open('estudantes.csv', 'r') as arquivo_estudantes:
    linhas = arquivo_estudantes.read().splitlines()
        
processar = lambda linha: ( linha.split(',')[0],                 
                            list(map(float, linha.split(',')[1:] 
                           )))      
dados = list(map(processar, linhas))                        
dados = sorted(dados, key=lambda x: x[0])                   

# processa cada estudante e imprime o resultado
for nome, notas in dados:
    top3 = list(map(int, sorted(notas, reverse=True)[:3]))  
    media = round(sum(top3) / 3, 2)                         
    print(f"Nome: {nome} Notas: {top3} Média: {media}")
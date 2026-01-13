with open("Sprint 4/Exercicios/ETL/actors.csv") as actors_file:
    linhas = actors_file.read().splitlines()[1:] 

contagem = {}
for linha in linhas:
    filme = linha.rsplit(',', 5)[4]
    contagem[filme] = contagem.get(filme, 0) + 1

resultado = sorted( contagem.items(), key=lambda x: (-x[1], x[0])) # usar -x[1] força a ordem decrescente da quantidade por meio da negação matemática
with open("Sprint 4/Exercicios/ETL/etapa-4.txt", "w", encoding="utf-8") as arquivo_saida:
    for filme, qtd in resultado:
        print(f"O filme {filme} aparece {qtd} vez(es) no dataset.", file=arquivo_saida)
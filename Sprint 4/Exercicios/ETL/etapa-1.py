with open("Sprint 4/Exercicios/ETL/actors.csv") as actors_file:
    linhas = actors_file.read().splitlines()[1:]

processar = lambda linha: (linha.rsplit(',', 5)[0],         # nome do ator
                           int(linha.rsplit(',', 5)[2]))    # número de filmes
dados  = list(map(processar, linhas))
ator_mais_filmes = max(dados, key=lambda x: x[1])

with open("Sprint 4/Exercicios/ETL/etapa-1.txt", "w", encoding="utf-8") as arquivo_saida:
    print(f"O ator que mais possui filmes no dataset é {ator_mais_filmes[0]}, com {ator_mais_filmes[1]} filmes.", file=arquivo_saida)
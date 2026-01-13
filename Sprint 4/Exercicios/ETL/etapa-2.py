with open("Sprint 4/Exercicios/ETL/actors.csv") as actors_file:
    linhas = actors_file.read().splitlines()[1:]

gross = map(
            lambda linha: float(linha.rsplit(',', 5)[5]), 
                                linhas
)

media = sum(gross) / len(linhas)

with open("Sprint 4/Exercicios/ETL/etapa-2.txt", "w", encoding="utf-8") as arquivo_saida:
    print(f"O valor médio de receita bruta dos principais filmes são de U$ {media:.2f} milhões de dólares.", file=arquivo_saida)
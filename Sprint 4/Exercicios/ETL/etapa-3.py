with open("Sprint 4/Exercicios/ETL/actors.csv") as actors_file:
    linhas = actors_file.read().splitlines()[1:]

dados = map(
            lambda linha: (
                            linha.rsplit(',', 5)[0], float(linha.rsplit(',', 5)[3])
                          ),
            linhas
            )
ator, maior_media = max(dados, key=lambda x: x[1])
with open("Sprint 4/Exercicios/ETL/etapa-3.txt", "w", encoding="utf-8") as arquivo_saida:
    print(f"O ator/atriz com maior média de receita bruta por filme é {ator} com média de {maior_media:.2f}", file=arquivo_saida)
with open("Sprint 4/Exercicios/ETL/actors.csv", encoding="utf-8") as actors_file:
    linhas = actors_file.read().splitlines()[1:]

atores = map(
    lambda linha: (
                    linha.split('"')[1] 
                        if linha.startswith('"') 
                        else linha.split(',', 1)[0],
                    float(
                        linha.rsplit(",", 5)[1]
                        .replace('"', '')
                        .strip()
                    )
    ),
    linhas
)

atores_ordenados = sorted(atores, key=lambda x: x[1], reverse=True)

with open("Sprint 4/Exercicios/ETL/etapa-5.txt", "w", encoding="utf-8") as arquivo_saida:
    for nome, total in atores_ordenados:
        arquivo_saida.write(f"{nome} - {total}\n")
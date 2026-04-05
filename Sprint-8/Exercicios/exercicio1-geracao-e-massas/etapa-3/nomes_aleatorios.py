import names, time, os, random
from tqdm import tqdm as progress_bar
# semente de aleatoriedade
random.seed(40)

qtd_nomes_unicos = 50000        # 50 mil
qtd_nomes_aleatorios = 1000000  # 1 milhão
dados = []

aux = [names.get_full_name() for _ in progress_bar(range(qtd_nomes_unicos), desc="Gerando nomes únicos")]

print(f'[LOADING] Gerando {qtd_nomes_aleatorios} nomes aleatórios')
with open('Sprint-8/Exercicios/exercicio1-geracao-e-massas/etapa-3/nomes_aleatorios.txt', 'w', encoding='utf-8') as file:
    for i in progress_bar(range(qtd_nomes_aleatorios), desc="Gerando nomes aleatórios:"):
        nome = random.choice(aux)
        file.write(nome + "\n")
print("\n [UPLOAD] Arquivo 'nomes_aleatorios.txt' gerado com sucesso!")


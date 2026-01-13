import random

random_list = random.sample(range(500), 50)
random_list = sorted(random_list)
qtd = len(random_list)

if qtd % 2 == 1:
    mediana = random_list[qtd // 2]
else:
    mediana = (random_list[qtd // 2 - 1] + random_list[qtd // 2]) / 2
media = sum(random_list)/qtd
valor_minimo = min(random_list)
valor_maximo = max(random_list)
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
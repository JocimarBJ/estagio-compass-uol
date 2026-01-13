with open("number.txt") as file:
    top5 = sorted(
           filter(lambda x: x % 2 == 0, map(int, file)),  # Converte para int e filtra pares
           reverse=True                                   # Ordena do maior para o menor
           )[:5]                                          # Pega os 5 primeiros (índices 0 a 4)

print(top5)
print(sum(top5))
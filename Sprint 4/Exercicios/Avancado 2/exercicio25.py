def maiores_que_media(conteudo:dict)->list:
    valores = list(map(lambda x: x[1], conteudo.items()))
    media = sum(valores) / len(valores)
    maiores = filter(lambda item: item[1] > media, conteudo.items())
    return sorted(list(maiores), key=lambda x: x[1])

conteudo = {
            "arroz":    4.99,
            "feijão":   3.49,
            "macarrão": 2.99,
            "leite":    3.29,
            "pão":      1.99
            }

print(maiores_que_media(conteudo))
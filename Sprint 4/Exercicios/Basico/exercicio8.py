def funcao(*args, **kwargs):
    for valor in args:
        print(valor)
    for chave, valor in kwargs.items():
        print(valor)
funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
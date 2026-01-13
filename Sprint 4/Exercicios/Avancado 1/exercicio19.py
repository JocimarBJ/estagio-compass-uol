class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor='azul'):
        self.modelo            = modelo
        self.velocidade_maxima = str(velocidade_maxima) + ' km/h'
        self.cor               = cor
        self.capacidade        = capacidade

aeroporto = [Aviao('BOIENG456', 1500, 400), 
             Aviao('Ebraer Praetor 600', 863, 14), 
             Aviao('Antonov An-2', 258, 12)]
for aviao in aeroporto:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {aviao.cor}')
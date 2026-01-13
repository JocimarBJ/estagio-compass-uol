from functools import reduce
def calcula_saldo(lancamentos) -> float:
    valores = map(lambda l: l[0] 
                            if l[1].lower()=='c' 
                            else -l[0],
                lancamentos)
    return reduce(lambda total, v: total + v, valores, 0)
    

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
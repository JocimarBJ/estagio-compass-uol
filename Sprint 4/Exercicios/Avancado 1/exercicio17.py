class Calculo:
    def soma(self, x, y):
        return x+y
    def subtracao(self, x, y):
        return x-y
x = 4; y = 5
calc = Calculo()
print(f'Somando: {x}+{y} = {calc.soma(x,y)}')
print(f'Subtraindo: {x}-{y} = {calc.subtracao(x,y)}')
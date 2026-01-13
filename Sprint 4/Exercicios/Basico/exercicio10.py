numeros_string = "1,3,4,6,10,76"
soma = sum(int(n) for n in numeros_string.split(','))
print(soma)
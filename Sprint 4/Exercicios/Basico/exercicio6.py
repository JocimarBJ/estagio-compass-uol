def my_map(lista, f):
    return list(f(num) for num in lista)

def exponenciar(num):
    return num ** 2

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(inteiros, exponenciar))
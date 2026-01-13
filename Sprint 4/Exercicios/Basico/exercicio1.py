a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = []
for i in a:
    if i % 2 != 0:
        impares.append(i)
"""
- OU
impares = [n for n in a if n % 2 != 0]
- OU
impares = list(filter(lambda i: i % 2 != 0, a))
"""
print(impares)
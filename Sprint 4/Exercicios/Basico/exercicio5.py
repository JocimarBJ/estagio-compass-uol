import json

with open('person.json', 'r') as arquivo_person:
    texto = arquivo_person.read()
    dados = json.loads(texto)

print(dados)

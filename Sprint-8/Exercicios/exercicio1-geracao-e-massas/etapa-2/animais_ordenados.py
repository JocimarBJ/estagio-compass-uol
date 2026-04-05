animais = [
    "Zebra", "Cachorro", "Gato", "Elefante", "Arara", 
    "Baleia", "Capivara", "Dromedário", "Foca", "Girafa", 
    "Hipopótamo", "Iguana", "Jacaré", "Leão", "Macaco", 
    "Onça", "Panda", "Quati", "Rato", "Sapo"
]

animais.sort()

[print(animal) for animal in animais]

with open("./Sprint-8/Exercicios/exercicio1-geracao-e-massas/etapa-2/lista_animais.txt", "w", encoding="utf-8") as file:
    for animal in animais:
        file.write(animal + "\n")
print("Arquivo 'lista_animais.txt' gerado com sucesso!")
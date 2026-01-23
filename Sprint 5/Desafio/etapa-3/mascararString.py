import hashlib as hl

while True:
    # Recebe a string
    entrada = input("Digite uma string (CTRL+C para sair): ")

    # Converte a string em Bytes (UTF-8) e gera o hash
    sha1_hash = hl.sha1(entrada.encode('utf-8')).hexdigest()

    # Exibe o hash gerado
    print("String mascarada (SHA-1):", sha1_hash)
    print("\n")
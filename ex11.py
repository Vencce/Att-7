try:
    with open("config.txt", "r") as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split("=")
            print(f"{chave}: {valor}")
except ValueError:
    print("Erro: Configuração mal formatada.")

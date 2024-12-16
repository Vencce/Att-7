dicionario = {"chave1": "valor1", "chave2": "valor2"}
try:
    chave = input("Digite uma chave: ")
    print(dicionario[chave])
except KeyError:
    print("Erro: Chave não encontrada.")

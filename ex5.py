try:
    with open("exemplo.txt", "x") as arquivo:
        arquivo.write("Teste.")
except FileExistsError:
    print("Erro: O arquivo já existe.")

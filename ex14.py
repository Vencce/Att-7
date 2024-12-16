try:
    senha = input("Digite uma senha: ")
    if len(senha) < 8:
        raise ValueError("Senha muito curta.")
    print("Senha válida.")
except ValueError as e:
    print(e)

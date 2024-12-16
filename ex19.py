try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro: Entrada inválida.")
else:
    print(f"Número válido: {numero}")


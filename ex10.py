try:
    numero = int(input("Digite um número: "))
    print(str(numero))
except ValueError:
    print("Erro: Valor digitado não é um número inteiro.")

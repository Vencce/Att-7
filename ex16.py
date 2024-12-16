try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Entrada inválida.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")

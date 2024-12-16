lista = [10, 20, 30, 40, 50]
try:
    indice = int(input("Digite um índice: "))
    print(lista[indice])
except IndexError:
    print("Erro: Índice fora dos limites da lista.")

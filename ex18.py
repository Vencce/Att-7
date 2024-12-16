try:
    try:
        lista = [1, 2, 3]
        print(lista[5])
    except IndexError:
        raise ValueError("Erro dentro do bloco aninhado.")
except ValueError as e:
    print(e)

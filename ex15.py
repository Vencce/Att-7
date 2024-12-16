def dividir_lista(lista, partes):
    try:
        tamanho = len(lista) // partes
        return [lista[i * tamanho:(i + 1) * tamanho] for i in range(partes)]
    except ZeroDivisionError:
        print("Erro: Número de partes inválido.")

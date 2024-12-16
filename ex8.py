class ListaInvalidaError(Exception):
    def __init__(self, mensagem="Lista inválida"):
        super().__init__(mensagem)

def ordenar_lista(lista):
    try:
        if not all(isinstance(x, str) for x in lista):
            raise ListaInvalidaError()
        return sorted(lista)
    except ListaInvalidaError as e:
        print(e)

class ArgumentoInvalidoError(Exception):
    def __init__(self, mensagem="Argumento inválido"):
        super().__init__(mensagem)

def contar_vogais(string):
    try:
        if not isinstance(string, str):
            raise ArgumentoInvalidoError()
        return sum(1 for char in string.lower() if char in "aeiou")
    except ArgumentoInvalidoError as e:
        print(e)

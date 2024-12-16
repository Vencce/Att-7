class ArgumentoInvalidoError(Exception):
    def __init__(self, mensagem="Argumento inválido"):
        super().__init__(mensagem)

def fatorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ArgumentoInvalidoError()
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    except ArgumentoInvalidoError as e:
        print(e)

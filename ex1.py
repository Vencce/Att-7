class DivisaoPorZeroError(Exception):
    def __init__(self, mensagem="Divisão por zero não permitida"):
        super().__init__(mensagem)

def dividir(a, b):
    try:
        if b == 0:
            raise DivisaoPorZeroError()
        return a / b
    except DivisaoPorZeroError as e:
        print(e)

from datetime import datetime

class DataInvalidaError(Exception):
    def __init__(self, mensagem="Data inválida"):
        super().__init__(mensagem)

def verificar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        print("Data válida.")
    except ValueError:
        raise DataInvalidaError()

# Exemplo
try:
    verificar_data("31/02/2024")
except DataInvalidaError as e:
    print(e)

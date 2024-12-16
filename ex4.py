class ArquivoInvalidoError(Exception):
    def __init__(self, mensagem="Arquivo inválido"):
        super().__init__(mensagem)

def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        raise ArquivoInvalidoError()

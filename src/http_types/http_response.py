# Importando a tipagem de dicionário
from typing import Dict

# Definindo a classe HttpResponse
class HttpResponse:
    # Método de inicialização da classe
    def __init__(self, body: Dict, status_code: int) -> None:
        """
        Inicializa uma instância da classe HttpResponse.

        Args:
            body (Dict): O corpo da resposta.
            status_code (int): O código de status da resposta.
        """
        # Atribui o corpo da resposta ao atributo 'body'
        self.body = body
        # Atribui o código de status da resposta ao atributo 'status_code'
        self.status_code = status_code

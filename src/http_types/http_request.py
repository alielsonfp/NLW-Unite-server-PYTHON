# Importando a tipagem de dicionário
from typing import Dict

# Definindo a classe HttpRequest
class HttpRequest:
    # Método de inicialização da classe
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        """
        Inicializa uma instância da classe HttpRequest.

        Args:
            body (Dict, opcional): O corpo da requisição. Padrão é None.
            param (Dict, opcional): Os parâmetros da requisição. Padrão é None.
        """
        # Atribui o corpo da requisição ao atributo 'body'
        self.body = body
        # Atribui os parâmetros da requisição ao atributo 'param'
        self.param = param

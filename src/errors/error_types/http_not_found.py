# Definição da classe HttpNotFoundError, que representa um erro de não encontrado HTTP
class HttpNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        # Inicialização do objeto HttpNotFoundError
        super().__init__(message)  # Chama o construtor da superclasse Exception com a mensagem de erro fornecida
        self.message = message  # Atribui a mensagem de erro ao atributo 'message' da instância
        self.name = "Not Found"  # Define o nome do tipo de erro como 'Not Found'
        self.status_code = 404   # Define o código de status HTTP associado a este tipo de erro como 404 (Não encontrado)

# Definição da classe HttpConflictError, que representa um erro de conflito HTTP
class HttpConflictError(Exception):
    def __init__(self, message: str) -> None:
        # Inicialização do objeto HttpConflictError
        super().__init__(message)  # Chama o construtor da superclasse Exception com a mensagem de erro fornecida
        self.message = message  # Atribui a mensagem de erro ao atributo 'message' da instância
        self.name = "Conflict"   # Define o nome do tipo de erro como 'Conflict'
        self.status_code = 409   # Define o código de status HTTP associado a este tipo de erro como 409 (Conflito)

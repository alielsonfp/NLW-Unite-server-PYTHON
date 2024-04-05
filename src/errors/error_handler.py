# Importando a classe HttpResponse do módulo http_response
from src.http_types.http_response import HttpResponse
# Importando as classes HttpConflictError e HttpNotFoundError dos módulos http_conflict e http_not_found, respectivamente
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

# Definindo a função handle_error que recebe um objeto error e retorna uma resposta HTTP
def handle_error(error: Exception) -> HttpResponse:
    # Verifica se o erro é uma instância de HttpConflictError ou HttpNotFoundError
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        # Se for, retorna uma resposta HTTP com o título e detalhes do erro e o código de status HTTP do erro
        return HttpResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "details": error.message
                }]
            },
            status_code=error.status_code
        )
    
    # Se não for, retorna uma resposta HTTP com o título "error" e os detalhes do erro convertidos para string
    return HttpResponse(
        body={
            "errors": [{
                "title": "error",
                "details": str(error)
            }]
        }
    )

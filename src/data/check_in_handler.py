# Importando a classe `CheckInRepository` do arquivo check_ins_repository
from src.models.repository.check_ins_repository import CheckInRepository
# Importando as classes `HttpRequest` e `HttpResponse` dos arquivos http_request e http_response, respectivamente
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

# Definindo a classe `CheckInHandler`, que lida com operações relacionadas a check-ins
class CheckInHandler:
    def __init__(self) -> None:
        # Inicialização do repositório de check-ins
        self.__check_in_respository = CheckInRepository()

    # Método para registrar um novo check-in
    def registry(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo as informações do check-in do parâmetro "attendee_id" da requisição HTTP
        check_in_infos = http_request.param["attendee_id"]
        # Inserindo o check-in no repositório de check-ins
        self.__check_in_respository.insert_check_in(check_in_infos)
        
        # Retornando uma resposta HTTP indicando sucesso (status code 201)
        return HttpResponse(
            body=None,
            status_code=201
        )

# Importando o módulo `uuid` para gerar UUIDs únicos
import uuid
# Importando a classe `EventsRepository` do arquivo events_repository
from src.models.repository.events_repository import EventsRepository
# Importando as classes `HttpRequest` e `HttpResponse` dos arquivos http_request e http_response, respectivamente
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
# Importando a classe `HttpNotFoundError` do arquivo http_not_found para representar erro HTTP 404 (Não encontrado)
from src.errors.error_types.http_not_found import HttpNotFoundError

# Definindo a classe `EventHandler`, que lida com operações relacionadas a eventos
class EventHandler:
    def __init__(self) -> None:
        # Inicialização do repositório de eventos
        self.__events_repository = EventsRepository()

    # Método para registrar um novo evento
    def register(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo o corpo (body) da requisição HTTP
        body = http_request.body
        # Gerando um UUID único para o evento e associando-o ao corpo (body)
        body["uuid"] = str(uuid.uuid4())
        # Inserindo o evento no repositório de eventos
        self.__events_repository.insert_event(body)

        # Retornando uma resposta HTTP indicando sucesso (status code 200) e o ID do evento
        return HttpResponse(
            body={ "eventId": body["uuid"] },
            status_code=200
        )

    # Método para encontrar um evento pelo seu ID
    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo o ID do evento da requisição HTTP
        event_id = http_request.param["event_id"]
        # Obtendo o evento pelo seu ID
        event = self.__events_repository.get_event_by_id(event_id)
        # Se o evento não for encontrado, levanta um erro HTTP 404 (Não encontrado)
        if not event: 
            raise HttpNotFoundError("Evento não encontrado")

        # Obtendo o número de participantes inscritos no evento
        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        # Retornando o evento e suas informações em uma resposta HTTP com status 200 (OK)
        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200
        )

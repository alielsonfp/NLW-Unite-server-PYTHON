# Importando módulos necessários
import uuid  # Módulo para gerar UUIDs únicos
from src.models.repository.attendees_repository import AttendeesRepository  # Importando o repositório de participantes
from src.models.repository.events_repository import EventsRepository  # Importando o repositório de eventos
from src.http_types.http_request import HttpRequest  # Importando a classe HttpRequest para representar requisições HTTP
from src.http_types.http_response import HttpResponse  # Importando a classe HttpResponse para representar respostas HTTP
from src.errors.error_types.http_not_found import HttpNotFoundError  # Importando a classe HttpNotFoundError para representar erro HTTP 404 (Não encontrado)
from src.errors.error_types.http_conflict import HttpConflictError  # Importando a classe HttpConflictError para representar erro HTTP 409 (Conflito)

# Definindo a classe `AttendeesHandler`, que lida com operações relacionadas a participantes
class AttendeesHandler:
    def __init__(self) -> None:
        # Inicializando os repositórios de participantes e eventos
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    # Método para registrar um novo participante em um evento
    def registry(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo o corpo (body) e o ID do evento da requisição HTTP
        body = http_request.body
        event_id = http_request.param["event_id"]

        # Verificando se o evento está lotado
        event_attendees_count = self.__events_repository.count_event_attendees(event_id)
        if (
            event_attendees_count["attendeesAmount"]
            and event_attendees_count["maximumAttendees"] < event_attendees_count["attendeesAmount"]
        ):
            raise HttpConflictError("Evento Lotado")  # Lançando um erro HTTP 409 se o evento estiver lotado

        # Gerando um UUID único para o participante e associando-o ao evento
        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        # Inserindo o participante no repositório de participantes
        self.__attendees_repository.insert_attendee(body)

        # Retornando uma resposta HTTP indicando sucesso (status code 201)
        return HttpResponse(body=None, status_code=201)

    # Método para encontrar o crachá (badge) de um participante por ID
    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo o ID do participante da requisição HTTP
        attendee_id = http_request.param["attendee_id"]
        # Obtendo o crachá (badge) do participante pelo seu ID
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not badge:
            raise HttpNotFoundError("Participante nao encontrado")  # Levantando um erro HTTP 404 se o participante não for encontrado
    
        # Retornando o crachá do participante em uma resposta HTTP com status 200 (OK)
        return HttpResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title
                }
            },
            status_code=200
        )

    # Método para encontrar todos os participantes de um evento
    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        # Obtendo o ID do evento da requisição HTTP
        event_id = http_request.param["event_id"]
        # Obtendo todos os participantes do evento pelo seu ID
        attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)
        if not attendees:
            raise HttpNotFoundError("Participantes nao encontrados")  # Levantando um erro HTTP 404 se nenhum participante for encontrado

        # Formatando os dados dos participantes para a resposta HTTP
        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "checkedInAt": attendee.checkedInAt,
                    "createdAt": attendee.createdAt
                }
            )

        # Retornando os participantes formatados em uma resposta HTTP com status 200 (OK)
        return HttpResponse(
            body={ "attendees": formatted_attendees },
            status_code=200
        )

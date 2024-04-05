# Importando a biblioteca typing para definir tipos de dados
from typing import Dict
# Importando a função de manipulação de conexão do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler
# Importando a entidade Events do pacote entities do pacote models
from src.models.entities.events import Events
# Importando a entidade Attendees do pacote entities do pacote models
from src.models.entities.attendees import Attendees
# Importando a exceção IntegrityError do sqlalchemy.exc
from sqlalchemy.exc import IntegrityError
# Importando a exceção NoResultFound do sqlalchemy.orm.exc
from sqlalchemy.orm.exc import NoResultFound
# Importando o tipo de erro HttpConflictError do pacote error_types do pacote errors
from src.errors.error_types.http_conflict import HttpConflictError

# Definindo a classe EventsRepository para manipulação de dados de eventos
class EventsRepository:
    # Método para inserir um novo evento no banco de dados
    def insert_event(self, eventsInfo: Dict) -> Dict:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            try:
                # Criando uma nova instância de evento com as informações fornecidas
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                )
                # Adicionando o evento à sessão do banco de dados
                database.session.add(event)
                # Confirmar a transação no banco de dados
                database.session.commit()
                # Retornando as informações do evento como confirmação de inserção bem-sucedida
                return eventsInfo
            except IntegrityError:
                # Se ocorrer um erro de integridade (por exemplo, violação de chave única), levante um HttpConflictError
                raise HttpConflictError('Evento já cadastrado!')
            except Exception as exception:
                # Em caso de qualquer outro erro, faça rollback da transação e levante a exceção
                database.session.rollback()
                raise exception

    # Método para obter um evento pelo seu ID
    def get_event_by_id(self, event_id: str) -> Events:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            try:
                # Consultando o banco de dados para obter o evento pelo seu ID
                event = (
                    database.session
                        .query(Events)
                        .filter(Events.id==event_id)
                        .one()
                )
                # Retornando o evento obtido
                return event
            except NoResultFound:
                # Se nenhum evento for encontrado, retorne None
                return None

    # Método para contar a quantidade de participantes em um evento específico
    def count_event_attendees(self, event_id: str) -> Dict:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            # Consultando o banco de dados para contar a quantidade de participantes no evento especificado
            event_count = (
                database.session
                    .query(Events)
                    .join(Attendees, Events.id == Attendees.event_id)
                    .filter(Events.id==event_id)
                    .with_entities(
                        Events.maximum_attendees,
                        Attendees.id
                    )
                    .all()
            )
            # Verificando se há participantes no evento
            if not len(event_count):
                # Se não houver participantes, retorne um dicionário com a quantidade máxima de participantes e a quantidade atual como 0
                return {
                    "maximumAttendees": 0,
                    "attendeesAmount": 0,
                }
            # Se houver participantes, retorne um dicionário com a quantidade máxima de participantes e a quantidade atual
            return {
                "maximumAttendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count),
            }

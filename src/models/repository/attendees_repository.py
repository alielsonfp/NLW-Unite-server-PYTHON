# Importando os tipos de dados Dict e List do módulo typing
from typing import Dict, List
# Importando a função de conexão do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler
# Importando as entidades Attendees, CheckIns e Events do pacote entities do pacote models
from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from src.models.entities.events import Events
# Importando as exceções IntegrityError e NoResultFound do módulo exc do sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
# Importando o tipo de erro HttpConflictError do pacote error_types do pacote errors
from src.errors.error_types.http_conflict import HttpConflictError

# Definindo a classe AttendeesRepository para manipulação de dados de participantes
class AttendeesRepository:
    # Método para inserir um novo participante no banco de dados
    def insert_attendee(self, attendde_info: Dict) -> Dict:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            try:
                # Criando uma nova instância de participante com as informações fornecidas
                attendee = (
                    Attendees(
                        id=attendde_info.get("uuid"),
                        name=attendde_info.get("name"),
                        email=attendde_info.get("email"),
                        event_id=attendde_info.get("event_id")
                    )
                )
                # Adicionando o participante à sessão do banco de dados
                database.session.add(attendee)
                # Confirmar a transação no banco de dados
                database.session.commit()

                return attendde_info  # Retornando as informações do participante inserido
            except IntegrityError:
                # Se ocorrer um erro de integridade (por exemplo, violação de chave única), levante um HttpConflictError
                raise HttpConflictError('Participante já cadastrado!')
            except Exception as exception:
                # Em caso de qualquer outro erro, faça rollback da transação e levante a exceção
                database.session.rollback()
                raise exception

    # Método para obter o crachá de um participante pelo seu ID
    def get_attendee_badge_by_id(self, attendee_id: str):
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            try:
                # Consulta ao banco de dados para obter informações do participante e do evento associado
                attendee = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id == attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        )
                        .one()  # Obtendo exatamente um resultado
                )
                return attendee  # Retornando as informações do participante
            except NoResultFound:
                return None  # Se nenhum resultado for encontrado, retornar None

    # Método para obter os participantes de um evento pelo ID do evento
    def get_attendees_by_event_id(self, event_id: str) -> List[Attendees]:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            # Consulta ao banco de dados para obter informações dos participantes e seus check-ins associados
            attendees = (
                database.session
                    .query(Attendees)
                    .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                    .filter(Attendees.event_id == event_id)
                    .with_entities(
                        Attendees.id,
                        Attendees.name,
                        Attendees.email,
                        CheckIns.created_at.label('checkedInAt'),
                        Attendees.created_at.label('createdAt')
                    )
                    .all()  # Obtendo todos os resultados
            )
            return attendees  # Retornando a lista de participantes

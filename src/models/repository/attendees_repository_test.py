# Importando a biblioteca pytest para escrever testes
import pytest
# Importando a classe AttendeesRepository do módulo attendees_repository
from .attendees_repository import AttendeesRepository
# Importando a função connect_to_db do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler

# Estabelecendo conexão com o banco de dados
db_connection_handler.connect_to_db()

# Definindo um teste para inserir um novo participante no banco de dados
@pytest.mark.skip(reason="Novo Registro em banco de dados")
def test_insert_attendee():
    # ID do evento fictício para o qual o participante será registrado
    event_id = "meu-uuid-e-nois"
    # Informações do participante
    attendees_info = {
        "uuid": "Meu_uuid_attendee",
        "name": "atendee name",
        "email": "email@email.com",
        "event_id": event_id
    }
 
    # Inicializando o repositório de participantes
    attendees_repository = AttendeesRepository()
    # Inserindo o participante no banco de dados e recebendo a resposta
    response = attendees_repository.insert_attendee(attendees_info)
    # Exibindo a resposta
    print(response)

# Definindo um teste para obter o crachá de um participante pelo seu ID
@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    # ID do participante fictício
    attendde_id = "meu_uuid_attendee"
    # Inicializando o repositório de participantes
    attendees_repository = AttendeesRepository()
    # Obtendo o crachá do participante pelo seu ID
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)

    # Exibindo informações do participante e seu título (por exemplo)
    print(attendee) 
    print(attendee.title)
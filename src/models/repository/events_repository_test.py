# Importando a biblioteca pytest para escrever testes
import pytest
# Importando a função de manipulação de conexão do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler
# Importando o repositório de eventos do módulo events_repository
from .events_repository import EventsRepository

# Estabelecendo conexão com o banco de dados
db_connection_handler.connect_to_db()

# Definindo um teste para inserir um novo evento no banco de dados
@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    # Definindo os detalhes do evento
    event = {
        "uuid" : "Meu-uuid-e-nois2",
        "title": "meu title",
        "slug" : "meu-slug-aqui2",
        "maximum_attendees" : 20
    }

    # Inicializando o repositório de eventos
    events_repository = EventsRepository()
    # Inserindo o evento no banco de dados e recebendo a resposta
    response = events_repository.insert_event(event)
    # Exibindo a resposta
    print(response) 

# Definindo um teste para obter um evento pelo seu ID
@pytest.mark.skip(reason="Não necessito mais")
def test_get_event_by_id():
    # ID do evento a ser obtido
    event_id = "Meu-uuid-e-nois22323232"
    # Inicializando o repositório de eventos
    events_repository = EventsRepository()
    # Obtendo o evento pelo seu ID e recebendo a resposta
    response = events_repository.get_event_by_id(event_id)
    # Exibindo a resposta e o título do evento (por exemplo)
    print(response)
    print(response.title)

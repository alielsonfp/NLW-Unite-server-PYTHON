# Importando módulos e classes necessárias
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler
from src.errors.error_handler import handle_error

# Definindo um blueprint Flask para rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

# Rota para criar um novo evento
@event_route_bp.route("/events", methods=["POST"])
def create_event():
    try:
        # Cria um HttpRequest com o corpo da requisição
        http_request = HttpRequest(body=request.json)
        # Inicializa o manipulador de eventos
        event_handler = EventHandler()
        # Chama o método register para criar o evento
        http_response = event_handler.register(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

# Rota para obter detalhes de um evento pelo seu ID
@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        # Inicializa o manipulador de eventos
        event_handler = EventHandler()
        # Cria um HttpRequest com o ID do evento
        http_request = HttpRequest(param={ "event_id": event_id })
        # Chama o método find_by_id para obter os detalhes do evento
        http_response = event_handler.find_by_id(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

# Importando módulos e classes necessárias
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler
from src.errors.error_handler import handle_error

# Definindo um blueprint Flask para rotas relacionadas a participantes
attendees_route_bp = Blueprint("attendees_route", __name__)

# Rota para registrar novos participantes em um evento
@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendees(event_id):
    try:
        # Inicializa o manipulador de participantes
        attendees_handle = AttendeesHandler()
        # Cria um HttpRequest com o ID do evento e o corpo da requisição
        http_request = HttpRequest(param={ "event_id": event_id }, body=request.json)
        # Chama o método registry para registrar os participantes no evento
        http_response = attendees_handle.registry(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

# Rota para obter o crachá de um participante por ID
@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees_batch(attendee_id):
    try:
        # Inicializa o manipulador de participantes
        attendees_handle = AttendeesHandler()
        # Cria um HttpRequest com o ID do participante
        http_request = HttpRequest(param={ "attendee_id": attendee_id })
        # Chama o método find_attendee_badge para obter o crachá do participante
        http_response = attendees_handle.find_attendee_badge(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

# Rota para obter todos os participantes de um evento
@attendees_route_bp.route("/events/<event_id>/attendees", methods=["GET"])
def get_attendees(event_id):
    try:
        # Inicializa o manipulador de participantes
        attendees_handle = AttendeesHandler()
        # Cria um HttpRequest com o ID do evento
        http_request = HttpRequest(param={ "event_id": event_id })
        # Chama o método find_attendees_from_event para obter os participantes do evento
        http_response = attendees_handle.find_attendees_from_event(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

# Importando módulos e classes necessárias
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler
from src.errors.error_handler import handle_error

# Definindo um blueprint Flask para rotas relacionadas a check-ins
check_in_route_bp = Blueprint("check_in_route", __name__)

# Rota para realizar o check-in de um participante
@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    try:
        # Inicializa o manipulador de check-ins
        check_in_handler = CheckInHandler()
        # Cria um HttpRequest com o ID do participante
        http_request = HttpRequest(param={ "attendee_id": attendee_id })
        # Chama o método registry para realizar o check-in do participante
        http_response = check_in_handler.registry(http_request)
        # Retorna o corpo da resposta e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        # Em caso de exceção, chama o handle_error para gerenciar o erro
        http_response = handle_error(exception)
        # Retorna uma resposta JSON com o corpo do erro e o código de status HTTP
        return jsonify(http_response.body), http_response.status_code

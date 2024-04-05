# Importando a classe Flask do módulo flask
from flask import Flask
# Importando o módulo CORS do flask_cors para lidar com requisições de origem cruzada (Cross-Origin Resource Sharing)
from flask_cors import CORS
# Importando a função de conexão do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler

# Estabelecendo conexão com o banco de dados
db_connection_handler.connect_to_db()

# Inicializando o aplicativo Flask
app = Flask(__name__)
# Habilitando CORS para permitir requisições de origem cruzada
CORS(app)

# Importando os blueprints das rotas de eventos, participantes e check-ins
from src.main.routes.event_routes import event_route_bp
from src.main.routes.attendees_route import attendees_route_bp
from src.main.routes.check_in_routes import check_in_route_bp

# Registrando os blueprints no aplicativo Flask
app.register_blueprint(event_route_bp)
app.register_blueprint(attendees_route_bp)
app.register_blueprint(check_in_route_bp)

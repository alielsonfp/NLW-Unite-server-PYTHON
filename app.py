# Importando a aplicação Flask do módulo server do pacote main
from src.main.server.server import app

# Verificando se este script está sendo executado diretamente
if __name__ == "__main__":
    # Iniciando o servidor Flask
    # Configurando para que o servidor esteja disponível em todas as interfaces de rede (0.0.0.0)
    # e na porta 3000
    # Habilitando o modo de depuração para facilitar a depuração (debug)
    app.run(host="0.0.0.0", port=3000, debug=True)

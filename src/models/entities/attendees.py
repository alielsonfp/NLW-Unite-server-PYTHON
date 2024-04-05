# Importando a classe Base do módulo base do pacote settings do pacote models
from src.models.settings.base import Base
# Importando as classes Column, String, DateTime e ForeignKey do módulo sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
# Importando a função func do módulo sqlalchemy.sql
from sqlalchemy.sql import func

# Definindo a classe Attendees, que representa os participantes de um evento
class Attendees(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = "attendees"

    # Definindo as colunas da tabela
    id = Column(String, primary_key=True)  # ID único do participante
    name = Column(String, nullable=False)  # Nome do participante
    email = Column(String, nullable=False)  # Endereço de e-mail do participante
    event_id = Column(String, ForeignKey("events.id"))  # ID do evento ao qual o participante está associado
    created_at = Column(DateTime, default=func.now())  # Data e hora de criação do registro do participante

    # Método de representação da classe, usado para representação de texto do objeto
    def __repr__(self):
        # Retorna uma string representando o objeto Attendees com seu nome, email e ID do evento associado
        return f"Attendees [name={self.name}, email={self.email}, event_id={self.event_id}]"

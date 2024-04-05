# Importando a classe Base do módulo base do pacote settings do pacote models
from src.models.settings.base import Base
# Importando as classes Column, String, Integer, DateTime e ForeignKey do módulo sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
# Importando a função func do módulo sqlalchemy.sql
from sqlalchemy.sql import func

# Definindo a classe CheckIns, que representa os check-ins dos participantes em eventos
class CheckIns(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = "check_ins"

    # Definindo as colunas da tabela
    id = Column(Integer, primary_key=True)  # ID único do check-in
    created_at = Column(DateTime, default=func.now())  # Data e hora de criação do registro do check-in
    attendeeId = Column(String, ForeignKey("attendees.id"))  # ID do participante associado ao check-in

    # Método de representação da classe, usado para representação de texto do objeto
    def __repr__(self):
        # Retorna uma string representando o objeto CheckIns com o ID do participante associado
        return f"CheckIns [attendeeId={self.attendeeId}]"

# Importando a classe Base do módulo base do pacote settings do pacote models
from src.models.settings.base import Base
# Importando as classes Column, String e Integer do módulo sqlalchemy
from sqlalchemy import Column, String, Integer

# Definindo a classe Events, que representa os eventos no banco de dados
class Events(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = "events"

    # Definindo as colunas da tabela
    id = Column(String, primary_key=True)  # ID único do evento
    title = Column(String, nullable=False)  # Título do evento
    details = Column(String)  # Detalhes do evento
    slug = Column(String, nullable=False)  # Slug do evento
    maximum_attendees = Column(Integer)  # Número máximo de participantes permitidos no evento

    # Método de representação da classe, usado para representação de texto do objeto
    def __repr__(self):
        # Retorna uma string representando o objeto Events com o título e o número máximo de participantes permitidos
        return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}]"

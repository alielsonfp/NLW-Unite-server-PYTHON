# Importando a função de manipulação de conexão do módulo connection do pacote settings do pacote models
from src.models.settings.connection import db_connection_handler
# Importando a entidade CheckIns do pacote entities do pacote models
from src.models.entities.check_ins import CheckIns
# Importando a exceção IntegrityError do módulo exc do sqlalchemy
from sqlalchemy.exc import IntegrityError
# Importando o tipo de erro HttpConflictError do pacote error_types do pacote errors
from src.errors.error_types.http_conflict import HttpConflictError

# Definindo a classe CheckInRepository para manipulação de dados de check-in
class CheckInRepository:
    # Método para inserir um novo registro de check-in no banco de dados
    def insert_check_in(self, attendee_id: str) -> str:
        # Estabelecendo conexão com o banco de dados
        with db_connection_handler as database:
            try:
                # Criando uma nova instância de check-in com o ID do participante fornecido
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                # Adicionando o registro de check-in à sessão do banco de dados
                database.session.add(check_in)
                # Confirmar a transação no banco de dados
                database.session.commit()
                # Retornando o ID do participante como confirmação de inserção bem-sucedida
                return attendee_id
            except IntegrityError:
                # Se ocorrer um erro de integridade (por exemplo, violação de chave única), levante um HttpConflictError
                raise HttpConflictError('Check In já cadastrado!')
            except Exception as exception:
                # Em caso de qualquer outro erro, faça rollback da transação e levante a exceção
                database.session.rollback()
                raise exception

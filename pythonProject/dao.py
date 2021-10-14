from models import Jogo, Usuario

SQL_DELETA_JOGO = 'delete from jogo where id = %s'
SQL_CRIA_JOGO = 'INSERT into jogo (nome, categoria, console) values (%s, %s, %s)'
SQL_ATUALIZA_JOGO = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id=%s'

class JogoDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, jogo):
        cursor = self.__db.connection.cursor()

        if (jogo._id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo._nome, jogo._categoria, jogo._console, jogo._id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo._nome, jogo._categoria, jogo._console))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return jogo
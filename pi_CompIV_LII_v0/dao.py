from models import Profissional, Usuario

SQL_DELETA_PROF = 'delete from profissional where id = %s'
SQL_CRIA_PROF = 'INSERT into profissional (nome, categoria, descricao, cidade, telefone, email, avaliacao) VALUES (%s, %s, %s, %s, %s, %s, %s)'
SQL_ATUALIZA_PROF = 'UPDATE profissional SET nome=%s, categoria=%s, descricao=%s, cidade=%s, telefone=%s, email=%s, avaliacao=%s where id=%s'
SQL_BUSCA_PROFS = 'SELECT id, nome, categoria, descricao, cidade, telefone, email, avaliacao from profissional'
SQL_USUARIO_POR_ID = 'SELECT id, nome, email, senha from usuario where id=%s'

class ProfDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, prof):
        cursor = self.__db.connection.cursor()

        if (prof._id):
            cursor.execute(SQL_ATUALIZA_PROF, (prof._nome, prof._categoria, prof._descricao, prof._cidade, prof._telefone, prof._email, prof._avaliacao, prof._id))
        else:
            cursor.execute(SQL_CRIA_PROF, (prof._nome, prof._categoria, prof._descricao, prof._cidade, prof._telefone, prof._email, prof._avaliacao))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return prof

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_PROFS)
        prof = traduz_profs(cursor.fetchall())
        return prof


def traduz_profs(profs):
    def cria_prof_com_tupla(tupla):
        return Profissional(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])
    return list(map(cria_prof_com_tupla, profs))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2], tupla[3])


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

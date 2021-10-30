class Profissional:
    def __init__(self, nome, categoria, descricao, cidade, telefone, email, avaliacao, id=None):
        self._id = id
        self._nome = nome
        self._categoria = categoria
        self._descricao = descricao
        self._cidade = cidade
        self._telefone = telefone
        self._email = email
        self._avaliacao = avaliacao

class Usuario:
    def __init__(self, id, nome, email, senha):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha = senha
import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `comp_civil`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `comp_civil`  DEFAULT CHARSET=utf8;
    USE `comp_civil`;
    CREATE TABLE `profissional` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `descricao` varchar(240) NOT NULL,
      `cidade` varchar(49) NOT NULL,
      `telefone` varchar(40) NOT NULL,
      `email` varchar(40) NOT NULL,
      `avaliacao` int(7) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;
    CREATE TABLE `usuario` (
      `id` varchar(8) NOT NULL,
      `nome` varchar(20) NOT NULL,
      `email` varchar(40) NOT NULL,
      `senha` varchar(8) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO comp_civil.usuario (id, nome, email, senha) VALUES (%s,%s, %s, %s)',
      [
            ('jgms', 'Joao Gabriel', 'jgms@gmail.com', '1223'),
            ('tadeu', 'Tadeu Tavarez', 'tadeu@gmail.com', '123456')
      ])

cursor.execute('select * from comp_civil.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo profissionais
cursor.executemany(
      'INSERT INTO comp_civil.profissional (nome, categoria, descricao, cidade, telefone, email, avaliacao) VALUES (%s, %s, %s, %s, %s, %s, %s)',
      [
            ('Jair', 'Pedreiro(a)', 'Jair o pedreiro trabalha com obras rapidas', 'Muzambinho - MG', '5535987654321', 'jair@gmail.com', '4'),
            ('Luiz', 'Eletricista', 'Jair o eletricista ideal para voce', 'Juruaia - MG', '5535987654312', 'luiz@gmail.com', '5'),
            ('Leandro', 'Pintor(a)', 'Leandro o pintor perfeito para lugares altos', 'Muzambinho - MG', '5535999654321', 'leandro@gmail.com', '4'),
            ('José', 'Carpinteiro(a)', 'Jose o mlehor carpinteiro da regiao', 'Guaxupe - MG', '5535987654333', 'jose@gmail.com', '2'),
            ('Guilherme', 'Outros', 'Guilherme, sempre pronto para instalar seu ar condicionado', 'São Paulo - SP', '5511988888888', 'gui@gmail.com', '3'),
            ('Fernanda', 'Marceneiro(a)', 'Fernanda especialista em moveis planejados', 'Juruaia - MG', '5535954641212', 'fer@gmail.com', '5')
      ])

cursor.execute('select * from comp_civil.profissional')
print(' -------------  Jogos:  -------------')
for profissional in cursor.fetchall():
    print(profissional[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
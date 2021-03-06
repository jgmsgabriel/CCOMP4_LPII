import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
'''conn.cursor().execute("DROP DATABASE `jogoteca`;")
conn.commit()'''

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `jogoteca`  DEFAULT CHARSET=utf8;
    USE `jogoteca`;
    CREATE TABLE `jogo` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;
    CREATE TABLE `usuario` (
      `id` varchar(8) NOT NULL,
      `nome` varchar(20) NOT NULL,
      `senha` varchar(8) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('diego', 'Diego Saqui', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Ação', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS'),
      ])

cursor.execute('select * from jogoteca.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
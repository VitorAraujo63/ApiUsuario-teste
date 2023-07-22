import sqlite3

conexao = sqlite3.connect('usuarios.db')

cursor =  conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
''')

dados_usuarios = [
    (1, 'Vitor', 'Araujo', 17),
    (2, 'Agatha', 'Rocha', 18),
    (12, 'Nilsa', 'Pereira', 34),
    (32, 'Alan', 'Silva', 22)
]

cursor.executemany('''
    INSERT INTO usuarios (id, nome, sobrenome, idade)
    VALUES (?, ?, ?, ?)
''', dados_usuarios)

conexao.commit()

conexao.close()
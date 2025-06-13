import sqlite3

conn = sqlite3.connect("db/database.db")
c = conn.cursor()

# Crear tabla de usuarios
c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insertar usuarios de prueba
c.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ('admin', 'admin123'))
c.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ('luis', 'powerup2025'))

conn.commit()
conn.close()
print("Base de datos inicializada.")

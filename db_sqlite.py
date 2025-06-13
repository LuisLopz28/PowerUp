# crear_db_sqlite.py
import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
''')

# Insertar un usuario de prueba
cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", ('admin', '1234'))

conn.commit()
conn.close()
print("✅ Base de datos SQLite creada con usuario admin.")

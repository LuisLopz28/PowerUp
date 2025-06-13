# database/db.py
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, select
import os

db_path = os.path.join(os.path.dirname(__file__), 'powerup.db')
engine = create_engine(f"sqlite:///{db_path}", echo=False)
metadata = MetaData()

# Define la tabla
usuarios = Table('usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String),
    Column('password', String)
)

# Crea la tabla si no existe
metadata.create_all(engine)

def verificar_usuario(username, password):
    with engine.connect() as conn:
        stmt = select(usuarios).where(
            (usuarios.c.username == username) &
            (usuarios.c.password == password)
        )
        result = conn.execute(stmt).fetchone()
        return result is not None

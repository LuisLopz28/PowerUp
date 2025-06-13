# insert_user.py
from sqlalchemy import create_engine, MetaData, Table
import os

db_path = os.path.join(os.path.dirname(__file__), 'database', 'powerup.db')
engine = create_engine(f"sqlite:///{db_path}", echo=True)
metadata = MetaData(bind=engine)
usuarios = Table('usuarios', metadata, autoload_with=engine)

# Insertar usuarios
with engine.connect() as conn:
    conn.execute(usuarios.insert().values(username="admin", password="admin123"))
    conn.execute(usuarios.insert().values(username="luis", password="powerup2025"))
    conn.commit()

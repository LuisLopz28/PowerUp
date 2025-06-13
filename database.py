import mysql.connector
from flask import g
from config import MYSQL_CONFIG

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**MYSQL_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

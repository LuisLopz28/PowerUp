import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-supersecreta-predeterminada'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

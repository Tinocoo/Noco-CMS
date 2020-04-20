import os


class BaseConfig(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@127.0.0.1/flaskadmin'
    FLASK_ADMIN_SWATCH = 'flatly'
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    BABEL_DEFAULT_TIMEZONE = 'America/Sao_Paulo'
    MODULES = [
        'login'
    ]

class ProductionConfig(BaseConfig):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@127.0.0.1/flaskadmin'
    FLASK_ADMIN_SWATCH = 'flatly'
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    BABEL_DEFAULT_TIMEZONE = 'America/Sao_Paulo'
    MODULES = [
        'login'
    ]

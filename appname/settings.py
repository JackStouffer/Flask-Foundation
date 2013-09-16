class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://example.db'
    SQLALCHEMY_ECHO = True
    CACHE_TYPE = 'null'

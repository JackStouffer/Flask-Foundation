class Config(object):
    SECRET_KEY = 'secret key'
    CACHE_TYPE = 'simple'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://example.db'
    SQLALCHEMY_ECHO = True

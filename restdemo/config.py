from datetime import timedelta
import os


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_URL_RULE = '/auth/login'
    JWT_AUTH_HEADER_PREFIX = os.environ.get('JWT_AUTH_HEADER_PREFIX', 'FLASK')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask123')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)


class TestingConfig(Config):
    """Config for testing"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(Config):
    """Config for Development"""
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.211.55.4:3306/api_demo'


class ProductionConfig(Config):
    ...


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

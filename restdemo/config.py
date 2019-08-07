from datetime import timedelta
import os


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_URL_RULE = '/auth/login'
    JWT_AUTH_ENDPOINT = 'JWT'
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)


class TestingConfig(Config):
    """Config for testing"""
    JWT_AUTH_ENDPOINT = 'FLASK'
    SECRET_KEY = "flask123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(Config):
    """Config for Development"""
    JWT_AUTH_ENDPOINT = 'FLASK'
    SECRET_KEY = "flask123"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@10.211.55.4:3306/api_demo"


class ProductionConfig(Config):
    ...


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
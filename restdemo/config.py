from datetime import timedelta
import os


class Config:
    #SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.211.55.4:3306/api_demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask123')
    JWT_AUTH_URL_RULE = '/auth/login'
    JWT_AUTH_ENDPOINT = 'JWT'
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)


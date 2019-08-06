from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from restdemo.resource.user import User, UserList


db = SQLAlchemy()

from restdemo.model.user import User as UserModel
from restdemo.model.demo import Demo

def create_app():

    app = Flask(__name__)
    api = Api(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@10.211.55.4:3306/api_demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')

    return app

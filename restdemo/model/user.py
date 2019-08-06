from datetime import datetime, timedelta

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from restdemo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))

    def __repr__(self):
        return "id={}, username={}".format(
            self.id, self.username
        )

    def as_dict(self):
        """使序列化返回字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def generate_token(self):
    #     """Generates the access token"""
    #     try:
    #         # set up a payload with an expiration time
    #         payload = {
    #             'exp': datetime.utcnow() + timedelta(minutes=5),
    #             'iat': datetime.utcnow(),
    #             'sub': self.username
    #         }
    #         # create the byte string token using the payload and the SECRET key
    #         jwt_token = jwt.encode(
    #             payload,
    #             current_app.config.get('SECRET'),
    #             algorithm='HS256'
    #         )
    #         return jwt_token.decode()
    #     except Exception as e:
    #         # return an error in string format if an exception occurs
    #         return str(e)

    @staticmethod
    def authenticate(username, password):
        user = db.session.query(User).filter(
            User.username == username
        ).first()
        if user:
            # check password
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = db.session.query(User).filter(
            User.id == user_id
        ).first()
        return user

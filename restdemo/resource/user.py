from flask_restful import Resource, reqparse
from flask import request, current_app
import jwt

from restdemo import db
from restdemo.model.user import User as UserModel

user_list = []

def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)
    return validate

class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'email', type=str, required=True, help='required email'
    )

    def get(self, username):
        """
        get user detail infomation
        """
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            return user.as_dict()
        return {'message': 'user not found'}, 404
    
    def post(self, username):
        """
        create a user
        """
        data = User.parser.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            return {"message": 'user already exist'}
        user = UserModel(
            username=username,
            email=data['email']
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return user.as_dict(), 201

    def delete(self, username):
        """
        delete user
        """
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            data = User.parser.parse_args()
            user.password_hash = data['password']
            db.session.commit()
            return user.as_dict()
        else:
            return {"message": 'user not found'}, 204

    def put(self, username):
        """
        update user
        """
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            data = User.parser.parse_args()
            user.password_hash = data['password']
            db.session.commit()
            return user.as_dict()
        else:
            return {'message': 'user not found'}, 204

class UserList(Resource):
    
    def get(self):
        token = request.headers.get('Authorization')
        try:
            jwt.decode(
                token,
                current_app.config.get('SECRET'),
                algorithms='HS256'
            )
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return {
                "message": "Expired token. Please login to get a new token"
            }
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return {
                "message": "Invalid token. Please register or login"
            }
        usres = db.session.query(UserModel).all()
        return [u.as_dict() for u in usres]

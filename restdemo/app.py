from flask import Flask
from flask_restful import Api

from resource.user import User, UserList
from resource.hello import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    app.run(debug=True)

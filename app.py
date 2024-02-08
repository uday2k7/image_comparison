import os
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SUPER-SECRET-KEY'
# Init db
db = SQLAlchemy(app)
jwt=JWTManager(app)


@app.route("/")
def welcome():
    return "Hello World"

from controllers import *


# Run Server
if __name__ == '__main__':
  app.run(debug=True)
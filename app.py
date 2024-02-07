from flask import Flask
import dataset
import sqlite3
#from flask_restful import Resource, Api


app = Flask(__name__)

#app.config['SECRET_KEY'] = 'SUPER-SECRET-KEY'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#db = dataset.connect('sqlite:///api.db')
     
@app.route("/")
def welcome():
    return "Hello World2"

# @app.route("/user/signup")
# def welcome():
#     db = dataset.connect('sqlite:///api.db')
#     return "Hello World2"


#import controller.user_controller as user_controller
#import controller.auth_controller as auth_controller
#from controller import user_controller, auth_controller
from controller import *


if __name__ ==  "__main__":
    app.run(debug=True)
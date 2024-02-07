from flask import Flask
#from flask_restful import Resource, Api


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World2"


#import controller.user_controller as user_controller
#import controller.auth_controller as auth_controller
#from controller import user_controller, auth_controller
from controller import *


if __name__ ==  "__main__":
    app.run(debug=True)
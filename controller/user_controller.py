from app import app
from flask import Flask, request
from validate_email import validate_email
from models.user_model import user_model
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required

jwt=JWTManager(app)
obj = user_model(jwt)

@app.route("/user/signup", methods=["POST"])
def Signup():
        return obj.Signup()
        # data = request.get_json()
        # username = data['username']
        # password = data['password']

        # return {'message':f'User created successfully {username}.'},200
        # is_valid=validate_email(username,verify=False)

        # if not username or not password:
        #     return {'message':'Missing username or password.'},400
        # if not is_valid:
        #     return {'message':'Invalid email address'},400
        #return obj.user_signup()
        # return obj.all_user_model()
        #return {'message':'User created successfully.'},200
        # if not username or not password:
        #     return {'message':'Missing username or password.'},400
        # if User.query.filter_by(username=username).first():
        #     return {'message':'Username already exists.'},400
        
        # new_user = User(username=username, password=password)
        # db.session.add(new_user)
        # db.session.commit()
        # return {'message':'User created successfully.'},200
@app.route("/user/login", methods=["POST"])
def Login():
        return obj.Login()

@app.route("/user/all")
# The endpoint for token_auth() is automatically getting calculated in the auth_model.token_auth() method
#@auth.token_auth()
def all_users():
    # res = flask.Response(obj.all_user_model())
    # res.headers["Content-type"] = "application/json"
    return obj.all_user_model()
from app import app
from flask import Flask, request
from validate_email import validate_email
from models.user_model import user_model


obj = user_model()

@app.route("/user/signup")
def user_controller_signup():
        # data = request.get_json()
        # username = data['username']
        # password = data['password']
       
        # is_valid=validate_email(username,verify=False)

        # if not username or not password:
        #     return {'message':'Missing username or password.'},400
        # if not is_valid:
        #     return {'message':'Invalid email address'},400
        return obj.user_signup()
        #return {'message':'User created successfully.'},200
        # if not username or not password:
        #     return {'message':'Missing username or password.'},400
        # if User.query.filter_by(username=username).first():
        #     return {'message':'Username already exists.'},400
        
        # new_user = User(username=username, password=password)
        # db.session.add(new_user)
        # db.session.commit()
        # return {'message':'User created successfully.'},200
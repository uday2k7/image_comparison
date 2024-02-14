import datetime
import hashlib
from app import db, app, request, jwt
from flask import Flask, request,jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, current_user
from validate_email import validate_email
from sqlalchemy import asc, desc
import uuid
import secrets
from controllers.Auth import * 



# class User(db.Model):
#     __tablename__ = 'users'
#     # user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id=db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
#     username=db.Column(db.String(100), unique=True, nullable=False)
#     password=db.Column(db.String(100), nullable=False)
#     firstname=db.Column(db.String(100), nullable=True)
#     lastname=db.Column(db.String(100), nullable=True)
#     user_role=db.Column(db.String(100), nullable=False)
#     email_confirmed=db.Column(db.Integer, default=0, nullable=False)
#     created_at=db.Column(db.String(100), nullable=False)

# with app.app_context():
#     db.create_all()

# class Usertoken(db.Model):
#     __tablename__ = 'user_tokens'
#     # user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id=db.Column(db.String(100), nullable=False, primary_key=True)
#     user_email=db.Column(db.String(100), nullable=False)
#     reset_token=db.Column(db.String(100), nullable=False)
#     requested_on=db.Column(db.String(100), nullable=True)

# with app.app_context():
#     db.create_all()


#List of all Users
# @app.route("/comparion/setbaseline/",defaults={'userId': None}, methods=["GET"])
@app.route("/comparion/setbaseline/", methods=["POST"])
@jwt_required()
def set_baseline():
    userDetails = get_jwt_identity()

    data = request.get_json()

    squadid = data['squadid']
    applicationid = data['applicationid']
    imagename = data['imagename']

    # create_directory(squadid)
    create_directory = create_comparison_directory(squadid,applicationid)
    if create_directory:
        return squadid+"--"+applicationid+"--"+imagename
    else:
        return {
            "success":False,
            "code":400,
            'message':"Problem creating directory."
        },400
    # create_directory(squadid+"/"+applicationid+"/Actuals")
    
    # current_roles = current_user()
    # return {'role':userDetails['role'],'user':userDetails['user']},200
    # try:
    #     userQuery=User.query
    #     if userId!=None:
    #         userQuery=userQuery.filter_by(user_id=userId).all()
    #     if userDetails['role'] == "Admin":
    #         userQuery = userQuery.order_by(asc(User.user_id)).all()

    #     userList = [
    #         dict(
    #             user_id=row.user_id, 
    #             username=row.username,
    #             password=row.password,
    #             role=row.user_role,
    #             email_confirmed=row.email_confirmed,
    #             created_at=row.created_at,
    #         )
    #         for row in userQuery
    #     ]
    #     return {
    #         "success":True,
    #         "code":200,
    #         'message':"",
    #         'data':userList
    #     },200
    # except:
    #     return jsonify({
    #         "success":False,
    #         "code":500,
    #         "message":"System encountered an unexpected problem and is being tracked.",
    #     }),200
    


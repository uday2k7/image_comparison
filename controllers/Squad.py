import datetime
import hashlib
from app import db, app, request, jwt
from flask import Flask, request,jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, current_user
from validate_email import validate_email
from sqlalchemy import asc, desc
import uuid
import secrets
# from controllers.Auth import * 



class Squad(db.Model):
    __tablename__ = 'squad'
    squad_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    # user_id=db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    squad_name=db.Column(db.String(100), unique=True, nullable=False)
    # password=db.Column(db.String(100), nullable=False)
    # firstname=db.Column(db.String(100), nullable=True)
    # lastname=db.Column(db.String(100), nullable=True)
    # user_role=db.Column(db.String(100), nullable=False)
    # email_confirmed=db.Column(db.Integer, default=0, nullable=False)
    # created_at=db.Column(db.String(100), nullable=False)

class Usersquad(db.Model):
    __tablename__ = 'user_squad'
    # user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_squad_id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(100), db.ForeignKey('users.user_id'))
    squad_id=db.Column(db.String(100), db.ForeignKey('squad.squad_id'))
    # created_at=db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


#Function to create user
@app.route('/squad/add', methods=['POST'])
def create_squad():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    squad_name = data['squad_name']

    if not squad_name:
        return {
            "success":False,
            "code":400,
            'message':"Missing Squad name."
        },400
        
    new_user = Squad(squad_name=squad_name)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"Squad added successfully."}),201

#Function to create user
@app.route('/usersquad/add', methods=['POST'])
def create_usersquad():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    squad_id = data['squad_id']
    user_id = data['user_id']
    # return squad_id;
    if not squad_id:
        return {
            "success":False,
            "code":400,
            'message':"Missing Squad id."
        },400
        
    new_user = Usersquad(squad_id=squad_id, user_id=user_id)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"Squad user added successfully."}),201

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
# @app.route("/user/list/",defaults={'userId': None}, methods=["GET"])
# @app.route("/user/list/<path:userId>", methods=["GET"])
# # @jwt_required()
# def list_user(userId):
#     # userDetails = get_jwt_identity()
#     # current_roles = current_user()
#     # return {'role':userDetails['role'],'user':userDetails['user']},200
#     # try:
#         userQuery=db.session.query(User)
#         # userQuery = userQuery.order_by(asc(User.user_id)).all()
#         # userQuery = userQuery.join(relatives, maindevotee.id == relatives.main_id)
#         userQuery = userQuery.join(Usersquad,Usersquad.user_id == User.user_id)
        
#         userList = [
#             dict(
#                 user_id=row.user_id,
#                 # username=row.username,
#                 # password=row.password,
#                 # role=row.user_role,
#                 # email_confirmed=row.email_confirmed,
#                 created_at=row.created_at,
#             )
#             for row in userQuery
#         ]
#         return {
#             # "success":True,
#             # "code":200,
#             # 'message':"",
#             'data':userList
#         },200
#     # except:
#     #     return jsonify({
#     #         "success":False,
#     #         "code":500,
#     #         "message":"System encountered an unexpected problem and is being tracked.",
#     #     }),200
    

# #List of all Users
# # @app.route("/user/list/",defaults={'userId': None}, methods=["GET"])
# @app.route("/user/edit/<path:userId>", methods=["POST"])
# @jwt_required()
# def edit_user(userId):
#     userDetails = get_jwt_identity()

#     data = request.get_json()
#     return userDetails['user']
#     # current_roles = current_user()
#     # return {'role':userDetails['role'],'user':userDetails['user']},200
#     # try:
#     #     userQuery=User.query
#     #     if userId!=None:
#     #         userQuery=userQuery.filter_by(user_id=userId).all()
#     #     if userDetails['role'] == "Admin":
#     #         userQuery = userQuery.order_by(asc(User.user_id)).all()

#     #     userList = [
#     #         dict(
#     #             user_id=row.user_id, 
#     #             username=row.username,
#     #             password=row.password,
#     #             role=row.user_role,
#     #             email_confirmed=row.email_confirmed,
#     #             created_at=row.created_at,
#     #         )
#     #         for row in userQuery
#     #     ]
#     #     return {
#     #         "success":True,
#     #         "code":200,
#     #         'message':"",
#     #         'data':userList
#     #     },200
#     # except:
#     #     return jsonify({
#     #         "success":False,
#     #         "code":500,
#     #         "message":"System encountered an unexpected problem and is being tracked.",
#     #     }),200
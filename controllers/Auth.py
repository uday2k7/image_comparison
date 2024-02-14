import datetime
import hashlib
from app import db, app, request, jwt
from flask import Flask, request,jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, current_user
from validate_email import validate_email
from sqlalchemy import asc, desc
import uuid
import secrets
from extras.utilities import *
from extras.uploadfile import *



class User(db.Model):
    __tablename__ = 'users'
    # user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id=db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(100), nullable=False)
    firstname=db.Column(db.String(100), nullable=True)
    lastname=db.Column(db.String(100), nullable=True)
    user_role=db.Column(db.String(100), nullable=False)
    email_confirmed=db.Column(db.Integer, default=0, nullable=False)
    created_at=db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

class Usertoken(db.Model):
    __tablename__ = 'user_tokens'
    # user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id=db.Column(db.String(100), nullable=False, primary_key=True)
    user_email=db.Column(db.String(100), nullable=False)
    reset_token=db.Column(db.String(100), nullable=False)
    requested_on=db.Column(db.String(100), nullable=True)

with app.app_context():
    db.create_all()


#Function to create user
@app.route('/user/signup', methods=['POST'])
def create_user():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    user_id = uuid.uuid4().hex
    username = data['username']
    # password_bytes = data['password'].encode('utf-8')
    # hash_object = hashlib.sha256(password_bytes)
    # password = hash_object.hexdigest()  
    password = encrypt_password(data['password'])  
    # return password
    user_role = data['role']
    firstName = data['firstname']
    lastName = data['lastname']
    
    is_valid=validate_email(username,verify=False)

    if not username or not password:
        return {
            "success":False,
            "code":400,
            'message':"Missing username or password."
        },400
        
    if not is_valid:
        return {
            "success":False,
            "code":400,
            'message':"Invalid email address."
        },400
        
    if User.query.filter_by(username=username).first():
        return {
                "success":False,
                "code":400,
                'message':"Username already exists."
            },400
    new_user = User(user_id=user_id, username=username, password=password, firstname=firstName, lastname=lastName, user_role=user_role, email_confirmed=0, created_at=currentTime)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"User added successfully."}),201

#Authentication function
@app.route("/user/login", methods=["POST"])
def Login():
    # try:
        email_confirmed = 0
        data = request.get_json()
        username = data['username']
        # password_bytes = data['password'].encode('utf-8')
        # hash_object = hashlib.sha256(password_bytes)
        password = encrypt_password(data['password'])

        user=User.query.filter_by(username=username).first()
       
        if User.query.filter_by(username=username, password=password).count() <= 0:
            return jsonify({
                "success":False,
                "code":404,
                "message":"Invalid username or password."
            }),200
        
        if user.email_confirmed == 0:
            return jsonify({
                "success":False,
                "code":404,
                "message":"Please activate your account."
            }),200
        
        if user.email_confirmed == 1 and user.password == password:
            access_token = create_access_token(identity ={'user':user.username,'role':user.user_role})
            data={
                "username":user.username,
                "displayname":user.firstname,
                "role":user.user_role,
            } 
        return jsonify({
            "success":True,
            "code":200,
            "message":"Login successful.",
            "access_token":access_token,
            "data":data
        }),200

@app.route('/user/tokenstatus', methods=['POST'])
def check_user_token():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    username = data['username']
    # reset_token = uuid.uuid4().hex[:6].upper()
    # reset_token = uuid.uuid4().hex+'-'+secrets.token_hex(200)
    reset_token = secrets.token_hex(50)
    # return reset_token
    
    if User.query.filter_by(username=username).count() > 0:
        user = User.query.filter_by(username=username).first()
        if Usertoken.query.filter_by(user_id=user.user_id).count() <= 0:        
            if user.user_id :
                new_user = Usertoken(user_id=user.user_id, user_email=username, reset_token=reset_token, requested_on=currentTime)
                db.session.add(new_user)
                db.session.commit()

                # user = Usertoken.query.filter_by(user_id=user.user_id).first()
        return jsonify({
            "success":True,
            "code":200,
            "message":"",
            "tokenExist":False
        }),200
    else:
        return jsonify({
            "success":False,
            "code":200,
            "message":"Invalud email ID.",
        }),200
    
@app.route('/user/changepassword', methods=['POST'])
def change_password():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    username = data['username']
    token = data['token']
    # password_bytes = data['password'].encode('utf-8')
    # hash_object = hashlib.sha256(password_bytes)
    # password = hash_object.hexdigest()  
    password = encrypt_password(data['password'])

    if Usertoken.query.filter_by(reset_token=token).count():

        update_password = User.query.filter_by(username=username).one()
        update_password.password = password
        db.session.commit()

        Usertoken.query.filter_by(user_email = username).delete()
        db.session.commit()
        return jsonify({
            "success":True,
            "code":200,
            "message":"Password updated successfully."
        }),200
    else:
        return jsonify({
            "success":False,
            "code":404,
            "message":"Invalid token."
        }),200
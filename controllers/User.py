import datetime
import hashlib
from app import db, app, request, jwt
from flask import Flask, request,jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
from validate_email import validate_email



class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(100), nullable=False)
    userRole=db.Column(db.String(100), nullable=False)
    emailConfirmed=db.Column(db.Integer, default=0, nullable=False)
    createdAt=db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()


#Function to create user
@app.route('/user/signup', methods=['POST'])
def create_user():
    currentTime = datetime.datetime.now()
    data = request.get_json()
    username = data['username']
    password_bytes = data['password'].encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    password = hash_object.hexdigest()  
    userRole = data['role']
    
    is_valid=validate_email(username,verify=False)

    if not username or not password:
        return {'message':'Missing username or password.'},400
    if not is_valid:
        return {'message':'Invalid email address'},400
    if User.query.filter_by(username=username).first():
        return {'message':'Username already exists.'},400
    new_user = User(username=username, password=password, userRole=userRole, emailConfirmed=0, createdAt=currentTime)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"User added successfully."}),201

#Authentication function
@app.route("/user/login", methods=["POST"])
def Login():
    try:
        emailConfirmed = 0
        data = request.get_json()
        username = data['username']
        password_bytes = data['password'].encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password = hash_object.hexdigest() 

        user=User.query.filter_by(username=username).first()
        data={
            "username":user.username,
            "token":"aa",
            "displayname":"aa",
            "email":"aa",
            "role":"aa",
            "photourl":"aa",
        }
        if user.emailConfirmed == 0:
            return jsonify({
                "success":False,
                "code":404,
                "message":"Please activate your account."
            }),200
           
        if user.emailConfirmed == 1 and user.password == password:
            access_token = create_access_token(identity =user.username)
        return jsonify({
            "success":True,
            "code":200,
            "message":"Login successful.",
            "access_token":access_token,
            "data":data
        }),200
    except:
        return jsonify({
            "success":False,
            "code":500,
            "message":"System encountered an unexpected problem and is being tracked.",
        }),200
    
#List of all Users
@app.route("/user/list", methods=["GET"])
@jwt_required()
def list_user():
    try:
        query=User.query.all()
        users = [
            dict(
                id=row.id, 
                username=row.username,
                password=row.password,
                role=row.userRole,
                emailConfirmed=row.emailConfirmed,
                createdAt=row.createdAt,
            )
            for row in query
        ]
        return {
            "success":True,
            "code":200,
            'message':"",
            'data':users
        },200
    except:
        return jsonify({
            "success":False,
            "code":500,
            "message":"System encountered an unexpected problem and is being tracked.",
        }),200
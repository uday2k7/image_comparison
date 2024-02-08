import datetime
import hashlib
from app import db,app, request
from flask import Flask, request,jsonify

#db = SQLAlchemy(app)
# User Class/Model
class User(db.Model):
    #return jsonify({"data":"user_list"})
#     __tablename__ = 'users'
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(100), unique=True, nullable=False)
#     password=db.Column(db.String(100), nullable=False)
#     userRole=db.Column(db.String(100), nullable=False)
#     emailConfirmed=db.Column(db.Integer, default=0, nullable=False)
#     createdAt=db.Column(db.String(100), nullable=False)

# with app.app_context():
#     db.create_all()
    
    @app.route('/user/signup', methods=['POST'])
    def create_user():
        return jsonify({"message":"create_user model."}),201
        currentTime = datetime.datetime.now()
        data = request.get_json()
        username = data['username']
        password_bytes = data['password'].encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password = hash_object.hexdigest()  
        userRole = data['role']
        
        new_user = User(username=username, password=password, userRole=userRole, emailConfirmed=1, createdAt=currentTime)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message":"User added successfully."}),201
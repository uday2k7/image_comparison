import sqlite3
#from flask_restful import Resource
#from flask import request
from flask import Flask, request
from configs.config import dbconfig
from validate_email import validate_email
import hashlib
import datetime
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required


class user_model():
    def __init__(self,jwt):   
        # conn = sqlite3.connect("image_comparison.sqlite")    
        # self.conn = sqlite3.connect("image_comparison.sqlite")     
        # self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        # self.con.autocommit=True
        # self.cur = self.con.cursor(dictionary=True)
        self.jwt = jwt
         
    #     # self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
    #     self.con.autocommit=True
        # self.cur = self.con.cursor(dictionary=True)
    # def db_connection():
    #     conn = None
    #     try:
    #         conn = sqlite3.connect("image_comparison.sqlite")
    #     except sqlite3.error as e:
    #         print(e)
    #     return conn

    def Signup(self):
        # conn = None
        # try:
        conn = sqlite3.connect("image_comparison.sqlite")
        # except sqlite3.error as e:
            # print(e)
        # return conn
        # conn = db_connection()
        cursor = conn.cursor()

        data = request.get_json()
        username = data['username']
        # password = data['password']
        password_bytes = data['password'].encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password = hash_object.hexdigest()  
        userRole = data['role']
        emailConfirmed = 0
        createdAt = datetime.datetime.now()

        is_valid=validate_email(username,verify=False)

        if not username or not password:
            return {'message':'Missing username or password.'},400
        if not is_valid:
            return {'message':'Invalid email address'},400
    
        sql = """INSERT INTO users (username, password, userRole, emailConfirmed, createdAt)
                 VALUES (?, ?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (username, password, userRole, emailConfirmed, createdAt))
        conn.commit()
        cursor.close()
        conn.close()
        
        return {'message':'User created successfully.'},200
    
    def Login(self):
        # conn = None
        # try:
        
        conn = sqlite3.connect("image_comparison.sqlite")
        # except sqlite3.error as e:
            # print(e)
        # return conn
        # conn = db_connection()
        cursor = conn.cursor()
        emailConfirmed = 0

        data = request.get_json()
        username = data['username']
        password_bytes = data['password'].encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password = hash_object.hexdigest() 
        # password_bytes = data['password'].encode('utf-8')
        # hash_object = hashlib.sha256(password_bytes)
        # password = hash_object.hexdigest()  

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        rows = cursor.fetchall()
        # conn.commit()
        # cursor.close()
        # conn.close()
        for r in rows:
            user = r
        # return {'token':user[4]},200
        # if book is not None:
        #     return jsonify(book), 200
        # else:
        #     return "Something wrong", 404
        #email_confirmed=user.emailConfirmed

        if user[4] == 0:
            return {'message':'Please activate your account'},400
        if user[4] == 1 and user[2] == password:
            access_token = create_access_token(identity =user[1])
            return {'message':'Login successful.','token':access_token},200

        #     return {'token':access_token},200
       
        return {'message':'Invalid credential.'},401
    
        # sql = """INSERT INTO users (username, password, userRole, emailConfirmed, createdAt)
        #          VALUES (?, ?, ?, ?, ?)"""
        # cursor = cursor.execute(sql, (username, password, userRole, emailConfirmed, createdAt))
        # conn.commit()
        # cursor.close()
        # conn.close()
        
        # return {'message':'User created successfully.'},200
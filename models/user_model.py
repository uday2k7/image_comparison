import sqlite3
#from flask_restful import Resource
#from flask import request
from flask import Flask, request
from configs.config import dbconfig
from validate_email import validate_email
import hashlib
import datetime

class user_model():
    # def __init__(self):   
        # conn = sqlite3.connect("image_comparison.sqlite")    
        # self.conn = sqlite3.connect("image_comparison.sqlite")     
        # self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        # self.con.autocommit=True
        # self.cur = self.con.cursor(dictionary=True)
         
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

    def signup(self):
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
        # self.cur.execute("SELECT * FROM users")
        # result = self.cur.fetchall()
        # if len(result)>0:
        #     return {"payload":result}
        #     # return make_response({"payload":result},200)
        # else:
        #     return "No Data Found"
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
from controllers.Squad import * 



#List of all Users
@app.route("/usersquad/list/",defaults={'userId': None}, methods=["GET"])

def list_user(userId):   
        userQuery=db.session.query(Usersquad)
        userQuery = userQuery.join(User,Usersquad.user_id == User.user_id)
        userQuery = userQuery.join(Squad,Usersquad.squad_id == Squad.squad_id)
        
        userList = [
            dict(
                user_squad_id=row.user_squad_id,
                user_id=row.user_id,
                squad_id=row.squad_id,
                # squad_name=row.squad_name,
            )
            for row in userQuery
        ]
        return {
            'data':userList
        },200

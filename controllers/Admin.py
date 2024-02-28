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



#List of all Users
@app.route("/admin/userlist", methods=["GET"])
@jwt_required()
def list_admin_user():
    identity = get_jwt_identity()
    # print(jwt)
    if identity['role'] == "Admin":
        return jsonify({
            "success":True,
            "code":200,
            "message":"Access permitted."
        }),200
    else:
        return jsonify({
            "success":True,
            "code":200,
            "message":"Access not permitted."
        }),200
    # userDetails = get_jwt_identity()
    # current_roles = current_user()
    # return {'role':userDetails['role'],'user':userDetails['user']},200
    # try:
    # try:
    #     return {
    #         "success":True,
    #         "code":200,
    #         'message':"Dummy Super Admin Access"
    #     },200
    # except:
    #     return jsonify({
    #         "success":False,
    #         "code":500,
    #         "message":"System encountered an unexpected problem and is being tracked.",
    #     }),200
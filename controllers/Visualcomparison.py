import datetime
import hashlib
from app import db, app, request, jwt, basedir
from flask import Flask, request,jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, current_user
from validate_email import validate_email
from sqlalchemy import asc, desc
import uuid
import secrets
from controllers.Auth import * 
# import json
import requests
# from datetime import datetime



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
@app.route("/comparion/setbaseline/", methods=['POST'])
@jwt_required()
def set_baseline():
    userDetails = get_jwt_identity()

    squadid = request.form['squadid']
    applicationid = request.form['applicationid']
    imagefile = request.files['imagefile']
    # upload_root_path = squadid+'/'+applicationid+'/Baseline'
    upload_root_path = 'uploads/'+squadid+'/'+applicationid
    # create_directory = create_comparison_directory(squadid,applicationid)
    create_directory = create_comparison_directory(upload_root_path)
    # return create_directory
    # upload_file(imagename,'uploads/squadid2/applicationid2/Baseline')
    # return "p"
    # create_directory = create_comparison_directory(squadid,applicationid)
    # print(create_directory)
    # return create_directory
    # if create_directory not 'None':
    if (create_directory != 'None'):
        upload_file(imagefile,create_directory)
        return {
            "success":True,
            "code":200,
            'message':"Baseline created successfully."
        },200 
    else:
        return {
            "success":False,
            "code":400,
            'message':"Unable to create image."
        },400 
        # target = create_directory

        # file = request.files['avatar']

        # file_name = file.filename or ''

        # destination = '/'.join([target, file_name])
        # file.save(destination)
        # return file_name

        # return "cc"
    # print(request.form['squadid'])
    # return squadid+"##"+applicationid
    # data = request.get_json()
    # return data['squadid']
    # target = 'files'
    
    # file = request.files['avatar']
    
    # file_name = file.filename or ''
    
    # destination = '/'.join([target, file_name])
    # file.save(destination)
    # return file_name
    
    # data = request.get_json()
    # data = request.files

    # uploaded_file = request.files['document']
    # data = request.get_json()
    # filename = secure_filename(uploaded_file.filename)
    # uploaded_file.save(os.path.join('files', filename))
    # print(data)
    # return 'success'
    # squadid = data['squadid']
    # applicationid = data['applicationid']
    # imagename = data['imagename']
    #print(data)
    # return data
    # target = 'files'

    # file = request.files['avatar']

    # file_name = file.filename or ''

    # destination = '/'.join([target, file_name])
    # file.save(destination)
    # return file_name
    # create_directory(squadid)
    # create_directory = create_comparison_directory(squadid,applicationid)
    # if create_directory:
        # target = 'files'

        # file = request.files['avatar']

        # file_name = file.filename or ''

        # destination = '/'.join([target, file_name])
        # file.save(destination)
        # return file_name
        # file = request.files['avatar']
        # new_filename =  str(datetime.now().timestamp()).replace(".", "") # Generating unique name for the file
        # return new_filename
        # split_filename = file.filename.split(".") # Spliting ORIGINAL filename to seperate extenstion
        # ext_pos = len(split_filename)-1 # Canlculating last index of the list got by splitting the filname
        # ext = split_filename[ext_pos] # Using last index to get the file extension
        # db_path = f"uploads/{new_filename}.{ext}"
        # file.save(f"uploads/{new_filename}.{ext}")
        # return new_filename
        # return obj.upload_avatar_model(uid, db_path)
        # post(imagename)
        # return squadid+"--"+applicationid+"--"+imagename
    
        # def get_avatar(uid):
        # data = obj.get_avatar_path_model(uid)
        # root_dir = os.path.dirname(app.instance_path)
        # return send_file(f"{root_dir}{data['payload'][0]['avatar']}")
    # else:
    #     return {
    #         "success":False,
    #         "code":400,
    #         'message':"Problem creating directory."
    #     },400
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
    


import hashlib
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse

def encrypt_password(password):
    password_bytes = password.encode('utf-16')
    hash_object = hashlib.sha256(password_bytes)
    password = hash_object.hexdigest()  

    return password

def create_comparison_directory(squad,application):
    # list = ['Baseline','Actuals']
    basedir = "uploads/"+squad+"/"+application+"/Baseline"
    actualdir = "uploads/"+squad+"/"+application+"/Actuals"

    basedirstatus=False
    actualdirstatus=False
    if not os.path.isdir(basedir): 
        basedirstatus = os.makedirs(basedir)
        basedirstatus=True
    if not os.path.isdir(actualdir): 
        actualdirstatus = os.makedirs(actualdir)
        actualdirstatus=True
    
    if basedirstatus==True and actualdirstatus == True:
        return create_comparison_directory
    else:
        return 'None'

# def uploadimage(self):
#         parse = reqparse.RequestParser()
#         parse.add_argument('audio', type=werkzeug.FileStorage, location='files')

#         args = parse.parse_args()

#         stream = args['audio'].stream
#         wav_file = wave.open(stream, 'rb')
#         signal = wav_file.readframes(-1)
#         signal = np.fromstring(signal, 'Int16')
#         fs = wav_file.getframerate()
#         wav_file.close()
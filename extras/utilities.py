import hashlib
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse

def encrypt_password(password):
    password_bytes = password.encode('utf-16')
    hash_object = hashlib.sha256(password_bytes)
    password = hash_object.hexdigest()  

    return password

def create_comparison_directory(root_path):
    # list = ['Baseline','Actuals']
    # basedir = "uploads/"+squad+"/"+application+"/Baseline"
    basedir = root_path+"/Baseline"
    # actualdir = "uploads/"+squad+"/"+application+"/Actuals"
    actualdir = root_path+"/Actuals"

    # basedirstatus=False
    # actualdirstatus=False
    if not os.path.isdir(basedir): 
        os.makedirs(basedir)
        # basedirstatus=True
    # else:
    #     basedirstatus=False

    if not os.path.isdir(actualdir): 
        os.makedirs(actualdir)
        # actualdirstatus=True
    # else:
    #      actualdirstatus=False

    if os.path.exists(basedir) and os.path.exists(actualdir):
        return basedir
    else:
        return 'None'

    # if os.path.isdir(basedir) and os.path.isdir(actualdir):
    #     return 'error'
    # else:
    #     basedirstatus = os.makedirs(basedir)
    #     actualdirstatus = os.makedirs(actualdir)
    #     return basedir
    # if basedirstatus==True and actualdirstatus == True:
    #     return basedir
    # else:
    #     return 'None'

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
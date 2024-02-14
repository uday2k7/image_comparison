import hashlib
import os

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
        return True
    else:
        return False
    # actualdir = os.makedirs("uploads/"+squad+"/"+application+"/Actuals")
#    if not os.path.isdir("uploads/"+dirname): 
    
    # if the demo_folder2 directory is  
    # not present then create it. 
        # os.makedirs("uploads/"+squad+"/"+application+"/Baseline") 
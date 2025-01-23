import cv2 
import os
import sys
import gc
import librosa
import pickle
from scipy.stats import zscore

import numpy as np
from sklearn.model_selection import train_test_split

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import hashlib
import socket
from flask_mysqldb import MySQL
from flask import *
import numpy as np
import os
from functools import wraps
import webbrowser
import ctypes
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from flask_mysqldb import MySQL
from tqdm import tqdm
import hashlib
import controller as ct
import cv2
import mysql.connector as mssql

def getMachine_addr():
    os_type = sys.platform.lower()
    command = "wmic bios get serialnumber"
    return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

def getUUID_addr():
	os_type = sys.platform.lower()
	command = "wmic path win32_computersystemproduct get uuid"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

def extract_command_result(key,string):
    substring = key
    index = string.find(substring)
    result = string[index + len(substring):]
    result = result.replace(" ","")
    result = result.replace("-","")
    return result
def key_validate(str):
    conn = mssql.connect(
        user='root', password='root', host='localhost', database='matrimony'
        )
    cur = conn.cursor()
    private_key = extract_command_result("SerialNumber",getMachine_addr()) + extract_command_result("UUID",getUUID_addr())
    if private_key in str:
        cur.execute("select * from SOFTKEY where private_key = %s and public_key = %s",(md5(private_key),md5(extract_command_result(private_key,str))))
        data=cur.fetchone()
        if data:
            return True
        else:
            return False
    else:
        return False
    
def predict(to_predict_list):
    print(to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1, 7)
    loaded_model = pickle.load(open("../Models/model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    print(result[0])
    return result[0]

    

def md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

def get_ip_address_of_host():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        mySocket.connect(('10.255.255.255', 1))
        myIPLAN = mySocket.getsockname()[0]
    except:
        myIPLAN = '127.0.0.1'
    finally:
        mySocket.close()
    return myIPLAN


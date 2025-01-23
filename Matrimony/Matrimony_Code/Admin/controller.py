import cv2 
import os, sys
import random
import string
import os

import gc
import mysql.connector as mssql
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
from IPython.display import display
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import hashlib
import socket
global model
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import librosa
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
def train():

            # Load the dataset
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report
    labelencoder = LabelEncoder()
    import pickle

    df = pd.read_excel('../Dataset/fake1.xlsx')
    df.to_csv('../Dataset/csvfile4.csv', encoding='utf-8',index=False)
    df4 = pd.read_csv('../Dataset/csvfile4.csv')

    df = pd.read_excel('../Dataset/real1.xlsx')
    df.to_csv('../Dataset/csvfile3.csv', encoding='utf-8',index=False)
    df3 = pd.read_csv('../Dataset/csvfile3.csv')

    df = pd.read_excel('../Dataset/real2.xlsx')
    df.to_csv('../Dataset/csvfile2.csv', encoding='utf-8',index=False)
    df2 = pd.read_csv('../Dataset/csvfile2.csv')

    df = pd.read_excel('../Dataset/real3.xlsx')
    df.to_csv('../Dataset/csvfile1.csv', encoding='utf-8',index=False)
    df1 = pd.read_csv('../Dataset/csvfile1.csv')

    df1 = df1.append(df2,ignore_index=True)
    df1 = df1.append(df3,ignore_index=True)
    df1 = df1.append(df4,ignore_index=True)

    category_col =['caste1', 'degree', 'employed1', 'income1', 'mother1', 'occupation',
                'religion1','account']  

    
    mapping_dict ={} 
    for col in category_col: 
        df1[col] = labelencoder.fit_transform(df1[col]) 
    
        le_name_mapping = dict(zip(labelencoder.classes_, 
                            labelencoder.transform(labelencoder.classes_))) 
    
        mapping_dict[col]= le_name_mapping 

    X = df1.drop(['account'],axis=1)
    y = df1['account']
    X_train ,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=101)
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    prediction1 = rfc.predict(X_test)
    print(mapping_dict)
    # pickle.dump(rfc, open('model.pkl','wb'))










    
    
def save_model():
    return True


def plot_accuracy():
    image = cv2.imread('../Plots/loss.png')
    return image

def plot_loss():
    image = cv2.imread('../Plots/loss.png')
    return image

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


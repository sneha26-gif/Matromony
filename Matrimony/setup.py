import os,sys
os.system('python -m pip install zipfile')
os.system('python -m pip install hashlib')
os.system('python -m pip install MySQL-python')
os.system('python -m pip install pyzipper')
os.system('python -m pip install random')
os.system('python -m pip install string')
os.system('python -m pip install ctypes')
import ctypes
import tkinter as tk
import zipfile
import mysql.connector
import pandas as pd
import os
import hashlib
import time
from tkinter import filedialog
import subprocess
import pyzipper
from tkinter import font
from tkinter import messagebox
import mysql.connector
import key_validator as gk
import hashlib
import time
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
def md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()
def validate_key():
    key = key_entry.get()
    private_key = gk.extract_command_result("SerialNumber",gk.getMachine_addr()) + gk.extract_command_result("UUID",gk.getUUID_addr())
    if private_key in str(key):
        conn = mysql.connector.connect(
        user='root', password='root', host='localhost', database='sys'
        )
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        cursor.execute("create database if not exists matrimony")   
        conn = mysql.connector.connect(
        user='root', password='root', host='localhost', database='matrimony'
        )
        cursor = conn.cursor()
        #Creating table as per requirement
        cursor.execute("DROP TABLE IF EXISTS SOFTKEY")
        sql ='''CREATE TABLE SOFTKEY(
            ID int NOT NULL AUTO_INCREMENT,
            private_key VARCHAR(64) NOT NULL,
            public_key VARCHAR(64) not null,
            primary key (id)
            )'''
        cursor.execute(sql)
        
        cursor.execute("insert into SOFTKEY(private_key, public_key) values(%s,%s);",(md5(private_key),md5(gk.extract_command_result(private_key,key))))
        conn.commit()
        messagebox.showinfo("Success", "Key has been succesfully updated")
        key_label.pack_forget()
        key_entry.pack_forget()
        Key_Validate.pack_forget()
        filepath_label.pack(pady=10)
        browse_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "Key Invalid! Contact your software provider.")
    

def install_file():
    global process
    
    install_button.pack_forget()
    filepath = filepath_label["text"]
    output_text.pack(pady=10, fill=tk.BOTH, expand=True)
    root.update() 
    output_text.insert('end', "Installing necessary libraries and modules\n")
    root.update()
    output_text.insert('end', "Installing flask\n")
    root.update()
    os.system('python -m pip install flask')
    output_text.insert('end', "Installing joblib\n")
    root.update()
    os.system('python -m pip install joblib')
    output_text.insert('end', "Installing csv\n")
    root.update()
    os.system('python -m pip install csv')
    output_text.insert('end', "Installing numpy\n")
    root.update()
    os.system('python -m pip install numpy')
    output_text.insert('end', "Installing scikit-learn\n")
    root.update()
    os.system('python -m pip install scikit-learn')
    output_text.insert('end', "Installing functools\n")
    root.update()
    os.system('python -m pip install functools')
    output_text.insert('end', "Installing pickle\n")
    root.update()
    os.system('python -m pip install pickle')
    output_text.insert('end', "Installing flask_mysqldb\n")
    root.update()
    os.system('python -m pip install flask_mysqldb')
    output_text.insert('end', "Installing tqdm\n")
    root.update()
    os.system('python -m pip install tqdm')
    output_text.insert('end', "Installing pandas\n")
    root.update()
    os.system('python -m pip install pandas')
    output_text.insert('end', "Installing IPython\n")
    root.update()
    os.system('python -m pip install IPython')
    output_text.insert('end', "Installing socket\n")
    root.update()
    os.system('python -m pip install socket')
    output_text.insert('end', "Installing openpyxl\n")
    root.update()
    os.system('python -m pip install openpyxl')
    output_text.insert('end', "Installing webbrowser\n")
    root.update()
    os.system('python -m pip install webbrowser')
    output_text.insert('end', "Installing ctypes\n")
    root.update()
    os.system('python -m pip install ctypes')
    output_text.insert('end', "Installing werkzeug\n")
    root.update()
    os.system('python -m pip install werkzeug')
    output_text.insert('end', "Installing tensorflow\n")
    root.update()
    os.system('python -m pip install tensorflow')
    output_text.insert('end', "Installing opencv-python\n")
    root.update()
    os.system('python -m pip install opencv-python')
    output_text.insert('end', "Installing pillow\n")
    root.update()
    os.system('python -m pip install pillow')
    output_text.insert('end', "Finalising modules\n")
    root.update()
    time.sleep(5)
    output_text.insert('end', "Creating Database for Web stack application\n")
    root.update()
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='root', host='localhost', database='matrimony'
    )
    time.sleep(2)
    output_text.insert('end', "Creating User Database tables\n")
    root.update()
    time.sleep(2)
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user")
    #Closing the connection
    sql ='''CREATE TABLE user(
    ID int NOT NULL AUTO_INCREMENT,
    username VARCHAR(250) NOT NULL,
    password VARCHAR(1000) not null,
    email VARCHAR(250) not null,
    primary key (id)
    )'''
    cursor.execute(sql)
    output_text.insert('end', "Creating Admin data table\n")
    root.update()
    time.sleep(2)
    cursor.execute("DROP TABLE IF EXISTS admin")
    #Closing the connection
    sql ='''CREATE TABLE admin(
    ID int NOT NULL AUTO_INCREMENT,
    username VARCHAR(250) NOT NULL,
    password VARCHAR(1000) not null,
    email VARCHAR(250) not null,
    primary key (id)
    )'''
    cursor.execute(sql)
    cursor.execute("insert into admin(username,password,email) values (%s,%s,%s)",('admin',md5('admin123'),'admin@mail.com'))
    output_text.insert('end', "Creating Tester data table\n")
    root.update()
    time.sleep(2)
    cursor.execute("DROP TABLE IF EXISTS tester")
    #Closing the connection
    sql ='''CREATE TABLE tester(
    ID int NOT NULL AUTO_INCREMENT,
    username VARCHAR(250) NOT NULL,
    password VARCHAR(1000) not null,
    email VARCHAR(250) not null,
    primary key (id)
    )'''
    cursor.execute(sql)
    cursor.execute("insert into tester(username,password,email) values (%s,%s,%s)",('tester',md5('tester123'),'tester@mail.com'))
    conn.commit()
    time.sleep(2)
    time.sleep(5)
    conn.close()
    output = 'Extracting files to: ' + filepath + '\n'
    output_text.insert('end', output)
    root.update()
    output_text.insert('end', "Creating Tests data table\n")
    root.update()
    time.sleep(2)
    cursor.execute("DROP TABLE IF EXISTS tests")
    #Closing the connection
    sql ='''CREATE TABLE tests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    castes VARCHAR(255),
    degrees VARCHAR(255),
    employs VARCHAR(255),
    incomes VARCHAR(255),
    mothers VARCHAR(255),
    occs VARCHAR(255),
    religions VARCHAR(255),
    prediction VARCHAR(255),
    status VARCHAR(255)
)'''
    cursor.execute(sql)
    zip_path = 'matrimony.zip'
    destination_folder = filepath
    password = 'swift22taylor7@1989'
    with pyzipper.AESZipFile(zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
        extracted_zip.extractall(destination_folder,pwd=str.encode(password))
    output_text.insert('end', "Finalising..this may take few minutes...\n")
    root.update()
    time.sleep(12)
    messagebox.showinfo("Success", "Setup fully Complete")
    root.destroy()

def browse_file():
    filepath = filedialog.askdirectory()
    if filepath == "":
        messagebox.showerror("Error", "Select a Valid path")
    else:
        filepath_label.config(text=filepath)
        browse_button.pack_forget()
        install_button.pack(pady=10)

# Create a Tkinter window
root = tk.Tk()
root.title("Setup")
root.configure(bg="white")
root.geometry("800x600")
# Create the widgets
title_label = tk.Label(root, text="Fake Profile Detection in Matrimony", bg="white", font=font.Font(family="Segoe UI", size=24, weight="bold"))
key_label = tk.Label(root, text="Enter 64-length key", bg="white", font = font.Font(family="Segoe UI", size=12, weight="bold"))
key_entry = tk.Entry(root, show="*",width=64,font = font.Font(family="Segoe UI", size=12, weight="bold"),borderwidth=2)
Key_Validate = tk.Button(root, text="Validate Key", command=validate_key, width=20,font=font.Font(family="Segoe UI", size=12, weight="bold"))
filepath_label = tk.Label(root, text="Select Path to Install", bg="white",font=font.Font(family="Segoe UI", size=12, weight="bold"))
browse_button = tk.Button(root, text="Browse", command=browse_file, width=20,font=font.Font(family="Segoe UI", size=12, weight="bold"))
install_button = tk.Button(root, text="Install", command=install_file, width=20, bg="#428bca", fg="white", font=font.Font(family="Segoe UI", size=12, weight="bold"))
output_label = tk.Label(root, text="Output", bg="white")
output_text = tk.Text(root, height=10, bg="lightgray")

# Add the widgets to the window
title_label.pack(pady=20)
key_label.pack(pady=10)
key_entry.pack(pady=10)
Key_Validate.pack(pady=10)
#filepath_label.pack(pady=10)
#browse_button.pack(pady=10)
#install_button.pack(pady=10)
#output_label.pack(pady=10)
#output_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()

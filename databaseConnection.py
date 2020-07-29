import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
load_dotenv(dotenv_path='/home/pi/piot/.env')
class MySQLConn:
    conn = mysql.connector.connect(
    host= os.getenv("HOST"), 
    user= os.getenv("USERR"),
    password= os.getenv("PASSWORD") ,
    database= os.getenv("DATABASE"),
    port= os.getenv("PORT")
    )
  
    cursor = conn.cursor()

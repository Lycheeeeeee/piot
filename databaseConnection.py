
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
env_path = Path('/Users/khanhni/Workplace/piot/.env')
load_dotenv(dotenv_path=env_path)
print(os.getenv("USER"))
class MySQLConn:
    conn = mysql.connector.connect(
    host= os.getenv("HOST"), 
    user= os.getenv("USER"),
    password= os.getenv("PASSWORD") ,
    database= os.getenv("DATABASE"),
    port= os.getenv("PORT")
    )
  
    cursor = conn.cursor()
import mysql.connector
import requests
import json
import os
from datetime import datetime
#from sense_hat import SenseHat
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(verbose=True)
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
"""mydb = mysql.connector.connect(
  host= 'localhost',
  user= 'mysql',
  password= 'admin',
  database= 'temandhum',
  port= 3306
  )"""
class Monitor:
  #sense = SenseHat()
  
  
  #mycursor = mydb.cursor()
  def __init__(self, temperature, humidity):
    self.temperature = temperature
    self.humidity = humidity
    now = datetime.now()
    self.time = now.strftime("%m/%d/%Y, %H:%M:%S") 

  """def saveToDatabase(self):
    sql = "INSERT INTO records (temp, humi) VALUES (%d,%d)"
    val = (self.temperature, self.humidity)
    self.mycursor.execute(sql,val)
    self.mycursor.commit()"""

  def checkComfortableRange(self):
    with open('config.json') as configFile:
      data = json.load(configFile)
    if self.temperature < data['cold_max'] or self.temperature >data['hot_min']:
      return False
    return True

  def pushNotify(self):
    if not self.checkComfortableRange():
      url = "https://api.pushbullet.com/v2/pushes"
      header = {'Content-Type': 'application/json','access-token': os.getenv("ACCESS_TOKEN")}
      data = {"body":"The temperature is out of comfortable ranges","title":"Temperature Warning","type":"note"}
      res = requests.post(url, headers = header , json = data)
      print(res.text)


monitor = Monitor(5,70)
monitor.pushNotify()

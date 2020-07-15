import requests
import json
import os
from datetime import datetime
#from sense_hat import SenseHat
from dotenv import load_dotenv
from pathlib import Path
from databaseConnection import MySQLConn


class Monitor:
  sense = SenseHat()
  mysqlconn = MySQLConn()
  mydb = mysqlconn.conn
  now = datetime.now()
  time = now.strftime("%m/%d/%Y") 
  mycursor = mysqlconn.cursor
  #def __init__(self, temperature, humidity):
  #  self.temperature = temperature
  #  self.humidity = humidity
    

  def saveToDatabase(self):
    
    if self.checkComfortableRange():
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,true)"
      val = (self.time,self.sense.get_temperature(), self.sense.get_humidity())
    else:
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,false)"
      val = (self.time, self.sense.get_temperature(), self.sense.get_humidity()) 
    self.mycursor.execute(sql,val)
    self.mydb.commit()

  def checkComfortableRange(self):
    with open('config.json') as configFile:
      data = json.load(configFile)
    if self.sense.get_temperature() < data['cold_max'] or self.sense.get_temperature() >data['hot_min']:
      return False
    return True

  def didNotify(self):
    sql = "SELECT count(comfortable) FROM records WHERE records.comfortable is false"
    self.mycursor.execute(sql)
    result = self.mycursor.fetchone()
    if result == 0:
      return False
    return True

  def pushNotify(self):
    if not self.checkComfortableRange() and not self.didNotify():
      url = "https://api.pushbullet.com/v2/pushes"
      header = {'Content-Type': 'application/json','access-token': os.getenv("ACCESS_TOKEN")}
      data = {"body":"The temperature is out of comfortable ranges","title":"Temperature Warning","type":"note"}
      res = requests.post(url, headers = header , json = data)
      print(res.text)


monitor = Monitor()
monitor.saveToDatabase()
monitor.pushNotify()

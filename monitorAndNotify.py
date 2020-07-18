#!/usr/bin/python3
import requests
import json
import os
from datetime import datetime
from sense_hat import SenseHat
from dotenv import load_dotenv
from pathlib import Path
from databaseConnection import MySQLConn
from senseHatCalibration import Calibration

class Monitor:
  sense = SenseHat()
  cali = Calibration()
  real_temp = cali.get_accurate_temp()
  mysqlconn = MySQLConn()
  mydb = mysqlconn.conn
  now = datetime.now()
  time = now.strftime("%m/%d/%Y") 
  mycursor = mysqlconn.cursor
  #def __init__(self, temperature, humidity):
  #  self.temperature = temperature
  #  self.humidity = humidity
    

  def saveToDatabase(self):
    
    if self.comfortableRange():
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,true)"
      val = (self.time,self.real_temp, self.sense.get_humidity())
    else:
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,false)"
      val = (self.time, self.real_temp, self.sense.get_humidity()) 
    self.mycursor.execute(sql,val)
    self.mydb.commit()

  def comfortableRange(self):
    with open('config.json') as configFile:
      data = json.load(configFile)
    if self.real_temp < data['cold_max'] or self.real_temp >data['hot_min']:
      return False
    return True

  def notified(self):
    sql = """SELECT count(comfortable) FROM records WHERE records.comfortable is
    false and records.date %(date)s"""
    value= {'date':self.time}
    self.mycursor.execute(sql,value)
    result = self.mycursor.fetchone()
    if result[0] == 1:
      return False
    return True

  def pushNotify(self):
    if not self.comfortableRange() and not self.notified():
      url = "https://api.pushbullet.com/v2/pushes"
      header = {'Content-Type': 'application/json','access-token': os.getenv("ACCESS_TOKEN")}
      data = {"body":"The temperature is out of comfortable ranges","title":"Temperature Warning","type":"note"}
      res = requests.post(url, headers = header , json = data)
      print(res.text)


monitor = Monitor()
monitor.saveToDatabase()
monitor.pushNotify()

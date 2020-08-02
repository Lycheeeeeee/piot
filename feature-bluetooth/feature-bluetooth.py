import bluetooth
import time
import json
import os
from read_json import jsonHandler
from get_temperature_humidity import senseHatDataRetriever
from bluetooth_client import bluetoothClient

# Call the delegated functions from import

# Wait for system to boot up
time.sleep(20)

# Get rounded values of temperature and humidity from SenseHAT
retriever = senseHatDataRetriever()
current_temp = round(senseHatDataRetriever.get_true_temp())    
current_humidity = round(senseHatDataRetriever.get_current_humidity())

# Check temperature and humidity whether they're in range
msg = jsonHandler.checkRange(current_temp,current_humidity)

# Scan nearby devices and send a message through bluetooth
bluetoothClient.findDevices(msg)


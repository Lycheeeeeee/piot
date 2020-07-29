import bluetooth
import time
import json
import os
from read_json import jsonHandler
from get_temperature_humidity import senseHatDataRetriever
from bluetooth_client import bluetoothClient

# Call the delegated functions from import

# Get rounded values of temperature and humidity from SenseHAT
current_temp = round(senseHatDataRetriever.get_true_temp())    
current_humidity = round(senseHatDataRetriever.get_pressure())

# Check temperature and humidity whether they're in range
msg = jsonHandler.checkRange(current_temp,current_humidity)

# Scan nearby devices and send a message through bluetooth
bluetoothClient.findDevices(msg)


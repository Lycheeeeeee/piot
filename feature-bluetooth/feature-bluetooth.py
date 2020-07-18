import bluetooth
import time


print("Scanning...")
nearbyDevices = bluetooth.discover_devices()
print(nearbyDevices)

if len(nearbyDevices) > 0:
    macAddress = nearbyDevices[0]
    # finding all nearby devices
    # for macAddress in nearbyDevices:
    print("Found device with mac-address: " + macAddress)

        #when found, send message to the device
    port = 1
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((macAddress, port))
    print("Connected")
    sock.send("hello!!")
    print("Printed")
    sock.close()
        # finding the port
# service = bluetooth.find_service(address=macAddress)
# print(service)
# print("Port" + service[3])
    
        
else:
    print("No bluetooth device found")
# print("Sleeping for 10 seconds.")
# time.sleep(10)

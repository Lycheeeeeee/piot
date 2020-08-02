import bluetooth
import time
import subprocess
from sense_hat import SenseHat

# Create a class
class bluetoothClient:

    # Color initialization
    w = [255, 255, 255]     # White
    r = [255, 0, 0]         # Red
    b = [0, 0, 255]         # Blue

    # Bluetooth icon pixel matrix
    bluetooth_icon = [
    b,b,b,w,b,b,b,b,
    b,w,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,b,b,w,w,b,b,b,
    b,b,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,w,b,w,w,b,b,b,
    b,b,b,w,b,b,b,b,
    ]

    sense = SenseHat()
    @staticmethod
    def sendMessageTo(targetBluetoothMacAddress, msg):
        # Clear SenseHat
        SenseHat().clear()
        
        # Setup RFCOMM Bluetooth connection
        port = 1
        client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        client_socket.connect((targetBluetoothMacAddress, port))
        
        # Send message through the bluetooth socket
        client_socket.send(msg)

        # close the socket
        client_socket.close()

    @classmethod
    def findDevices(cls,msg):
        # # Wait for system
	    # time.sleep(10) 
        # Turn on Bluetooth
        subprocess.run("sudo rfkill unblock bluetooth", shell = True)
        time.sleep(1)

        # Start scaning and sending message
        while True:
            cls.sense.clear()
            cls.sense.set_pixels(cls.bluetooth_icon)
            nearbyDevices = bluetooth.discover_devices()

            if len(nearbyDevices) > 0:
                print(nearbyDevices)

                # Found all nearby devices
                for macAddress in nearbyDevices:
                    print("Found device with mac-address: " + macAddress)
                    print("Sending message to " + macAddress)
                    try:
                        bluetoothClient.sendMessageTo(macAddress, msg)
                    except Exception:
                        # Keep sending to other bluetooth devices
                        continue      
                
                break # Quit searching for devices to send

            # else: # Wait before trying searching again
            #     time.sleep(10)
import bluetooth
import time
import subprocess

# Create a class
class bluetoothClient:
    
    @staticmethod
    def sendMessageTo(targetBluetoothMacAddress, msg):
        # Setup RFCOMM Bluetooth connection
        port = 1
        client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        client_socket.connect((targetBluetoothMacAddress, port))
        
        # Send message through the bluetooth socket
        client_socket.send(msg)
        
        client_socket.close()

    @staticmethod
    def findDevices(msg):
        # Turn on Bluetooth
        subprocess.run("sudo rfkill unblock bluetooth", shell = True)
        time.sleep(1)

        # Start scaning and sending message
        while True:
            print("Scanning...")
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

            else: # Wait before trying searching again
                time.sleep(10)

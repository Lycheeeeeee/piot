import bluetooth
import subprocess
import time
from sense_hat import SenseHat
	
def receiveMessages():
	# Turn on Bluetooth
	subprocess.run("sudo rfkill unblock bluetooth", shell = True)
	time.sleep(1)

	# Turn on Discoverable mode
	subprocess.run("sudo hciconfig hci0 piscan", shell = True)
	
	# Setup RFCOMM Bluetooth connection	
	receiver_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port = 1

	# Bind the receiver socket and starts listening 
	receiver_socket.bind(("",port))
	receiver_socket.listen(1)
	sender_socket = receiver_socket.accept()

	# Receive the message from bluetooth sender
	data = sender_socket.recv(1024).decode()

	# Display message on SenseHAT
	sense = SenseHat()
	sense.show_message(str(data))
	
	# Close the bluetooth sockets
	sender_socket.close()
	receiver_socket.close()

# Execute the program
receiveMessages()
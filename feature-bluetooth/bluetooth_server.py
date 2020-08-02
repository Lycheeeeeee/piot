import bluetooth
import subprocess
import time
from sense_hat import SenseHat

# Color initialization
w = [255, 255, 255]     # White
r = [255, 0, 0]         # Red
b = [0, 0, 255]         # Blue


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

receiving = True

def receiveMessages():
	# Wait for system
	time.sleep(20) 

	# Turn on Bluetooth
	subprocess.run("sudo rfkill unblock bluetooth", shell = True)
	time.sleep(1)

	# Display Bluetooth icon on SenseHat
	sense = SenseHat()
	sense.set_pixels(bluetooth_icon)

	# Turn on Discoverable mode
	subprocess.run("sudo hciconfig hci0 piscan", shell = True)
	
	# Setup RFCOMM Bluetooth connection	
	receiver_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port = 1

	# Bind the receiver socket and starts listening 
	receiver_socket.bind(("",port))
	receiver_socket.listen(1)

	# Accept incoming connection
	sender_socket, address = receiver_socket.accept()

	# Pair the device
	# subprocess.run("sudo bluetoothctl; default-agent; trust {}; quit",\
    #          shell = True)
	# subprocess.run("sudo bluetoothctl", shell = True)
	# subprocess.run("default-agent", shell = True)
	
	# subprocess.run("trust {}".format(address), shell = True)
	# subprocess.run("quit", shell = True)

	# Receive the message from bluetooth sender
	data = str(sender_socket.recv(1024).decode())

	# Format the message
	message_list = data.split("|")
	temp_message = message_list[0]
	humidity_message = message_list[1]


	# Display message on SenseHAT
	sense.clear()
	sense.show_message(temp_message, scroll_speed=0.05, back_colour=w, text_colour=r)
	
	time.sleep(1)
	sense.show_message(humidity_message, scroll_speed=0.05, back_colour=w, text_colour=b)
	sense.clear()
	
	# Close the bluetooth sockets
	sender_socket.close()
	receiver_socket.close()

# Execute the program
receiveMessages()

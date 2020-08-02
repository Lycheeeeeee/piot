crontab -e
save to the database and push notification every minute
* * * * * python3 /home/pi/piot/monitorAndDisplay.py
read temperature and display every minute
* * * * * python3 /home/pi/piot/readAndDisplay.py
run the apiRESTful server whenever the pi is booted
@reboot python3 /home/pi/piot/apiRESTful.py

command request to test the API
GET the newest records:
  curl --location --request GET 'localhost:5000/get' \
  --header 'Content-Type: application/json' \
  --data-raw '
  '
POST upload the new record:
  curl --location --request POST 'localhost:5000/upload' \
  --header 'Content-Type: application/json' \
  --data-raw '{	
  "temperature":20,
	"comfortable":false,
	"date":"07/10/2020",
	"humidity":45
  }'

PUT update the newest record:
  curl --location --request PUT 'localhost:5000/update' \
  --header 'Content-Type: application/json' \
  --data-raw '{	
	"temperature":22,
	"comfortable":true,
	"humidity":55
  }
  '

----
FEATURE-BLUETOOTH:
Setup: 
a/ run script at startup by using crontab by typing the following command (in terminal): <!-- EDITOR=nano crontab -e -->
b/ on the client side, append the script to crontab including the path to feature_bluetooth.py:<!-- @reboot python3 path_to_file/feature_bluetooth.py >> path_to_output/cron_log.txt 2>1& -->
c/ on the server side, run bluetooth_server.py using crontab by typing the command:
    <!-- @reboot python3 path_to_file/feature_bluetooth.py 
    >> path_to_output/cron_log.txt 2>1& -->

Function:
a/ The scripts run at startup, and the client_side script will find the nearby devices, then send to the devices which are running the server_side script.
b/ Once connected, the client_side sends the message containing the temperature and humidity to the server_side.
----
FEATURE-GAME:
Setup: Run the game.py script on the Pi

Function:
a/ The game shows instructions to the players.
b/ The players take turn, and toggle SenseHat joystick (Left for Player 1, Right for Player 2) to shake the dice.
c/ First player to get 30 wins the game.
d/ The program write into .csv file the winner score and time stamp of the game.
----
REFERENCES:
PEP8 naming conventions
https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention

SenseHAT LED matrix
https://pythonhosted.org/sense-hat/api/#led-matrix

Python @staticmethod and @classmethod
https://stackoverflow.com/questions/1859959/static-methods-how-to-call-a-method-from-another-method

Class method and static method
https://realpython.com/instance-class-and-static-methods-demystified/

Python and Bluetooth
http://pages.iu.edu/~rwisman/c490/html/pythonandbluetooth.htm

Python time.sleep()
https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/

Python joy stick
https://pythonhosted.org/sense-hat/api/#joystick

Unix Bluetooth Turn On and Off
https://askubuntu.com/questions/450698/how-to-turn-on-and-off-bluetooth-visibility-mode

Unix Bluetooth Discoverable Mode
https://askubuntu.com/questions/450698/how-to-turn-on-and-off-bluetooth-visibility-mode

Unix subprocess.call (running Unix cmd commans using Python)
https://queirozf.com/entries/python-3-subprocess-examples

Handling errors and exception
https://docs.python.org/3/tutorial/errors.html

Getting correct file path
https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory

Getting Time stamp
https://www.programiz.com/python-programming/datetime/current-datetime

Scheduling tasks with Cron
https://www.raspberrypi.org/documentation/linux/usage/cron.md
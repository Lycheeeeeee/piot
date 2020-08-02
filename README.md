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


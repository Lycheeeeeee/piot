#crontab -e
vim editor
  * * * * * cd ~/ && ./runMonitor.sh
remember to chmod the .sh file
#crontab for display the temperature
  * * * * * cd ~/ && ./startDisplay.sh
#crontab for run the api server
  @reboot python3 /home/pi/piot/apiRESTful.py OR
  @reboot cd ~/ && ./api.sh

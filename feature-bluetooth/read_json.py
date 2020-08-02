import json
import os
from sense_hat import SenseHat

class jsonHandler:
    min_temp = 0
    max_temp = 0
    min_humidity = 0
    max_humidity = 0
    
    @classmethod
    def checkRange(cls, temp, humidity):
        try:
            
            current_directory = os.getcwd()
            file_name = current_directory + "/piot/feature-bluetooth/config_min_max.json"
            # Load the json file into python
            with open(file_name) as data_file:
                data = data_file.read()
                config_range = json.loads(data)    
            
            # Setting the variables
            cls.min_temp = config_range["min_temperature"]
            cls.max_temp = config_range["max_temperature"]
            cls.min_humidity = config_range["min_humidity"]
            cls.max_humidity = config_range["max_humidity"]

            temp_position = jsonHandler.checkTemp(temp)
            temp_message = "> Temperature is {} at {} degrees".format(temp_position, temp)
            humidity_position = jsonHandler.checkHumidity(humidity)
            humidity_message = "> Humidity is {} at {}%".format(humidity_position, humidity)

            # Return the message
            result = temp_message + " " + humidity_message
            return(result)

        except Exception as exception_message:
            SenseHat().show_message("Error: {}".format(exception_message))
            # print("Cannot load json due to exception {}".format(exception_message))

# Background logic
# Define methods to be called in the static method
    @classmethod
    def checkTemp(cls,temp):
        max = cls.max_temp
        min = cls.min_temp
        
        if temp > max:
            above_max_value = temp - max
            return("{} degrees above max temperature"
            .format(str(above_max_value)))
        
        elif temp == max:
            return("at the max temperature")
        
        else:
            if temp > min:
                above_min_value = temp - min
                below_max_value = max - temp
                if (above_min_value) < (below_max_value):
                    return("{} degrees above min temperature"
                    .format(str(above_min_value)))
                else:
                    return("{} degrees below max temperature"
                    .format(str(below_max_value)))

            elif temp == min:
                return("at the min temperature")
            else:
                below_min_value = min - temp
                return("{} degrees below min temperature"
                .format(str(below_min_value)))

    @classmethod
    def checkHumidity(cls, humidity):
        max = cls.max_humidity
        min = cls.min_humidity
        
        if humidity > max:
            above_max_value = humidity - max
            return("{} percent above max humidity"
            .format(str(above_max_value)))
        
        elif humidity == max:
            return("at the max humidity")
        
        else:
            if humidity > min:
                above_min_value = humidity - min
                below_max_value = max - humidity
                if (above_min_value) < (below_max_value):
                    return("{} percent above min humidity"
                    .format(str(above_min_value)))
                else:
                    return("{} percent below max humidity"
                    .format(str(below_max_value)))

            elif humidity == min:
                return("at the min humidity")
            else:
                below_min_value = min - humidity
                return("{} percent below min humidity"
                .format(str(below_min_value)))


    






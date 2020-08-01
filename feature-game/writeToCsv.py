import csv
from datetime import datetime
import os

class csvHandler:
    # Symbolic initialization
    index_numer = 0
    path = os.getcwd()
    file_dir = path + "/piot/feature-game/"
    file_name = file_dir + "winner.csv"

    @classmethod
    def getIndexNumber(cls):
        # Get ordering number
        try:
            with open(cls.file_name, "r", encoding = "utf-8") as data_read:
                data = data_read.readlines()
            # Get index from the last line of csv
            lastRow = data[-1]
            index_number = int((lastRow.split(","))[0]) + 1
        
        # If file has not existed, index is 1
        except FileNotFoundError:
            index_number = 1

        return index_number

    @classmethod  
    def writeToCsv(cls, game_result):
        # Get the current time stamp
        now = datetime.now()
        time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")
        
        index_number = cls.getIndexNumber()
        # Compile the message row
        row_contents = [index_number,game_result,time_stamp]
        
        # Append to the current file
        try:
            with open(cls.file_name, "a+", newline="") as writer_obj:
                csv_writer = csv.writer(writer_obj)
                csv_writer.writerow(row_contents)

        # If not created, create new file
        except FileNotFoundError:
            with open(cls.file_name, "w", newline="") as writer_obj:
                csv_writer = csv.writer(writer_obj)
                csv_writer.writerow(row_contents)

    
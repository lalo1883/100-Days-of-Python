#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager



sheet = DataManager()
data = sheet.get_data()

print(data)
from pprint import pprint
import requests
sheet_get_endopoint = f'https://api.sheety.co/3d8ebdedf54e4ec3992f394fd1a028da/flightDeals/prices'
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_data(self):
        response = requests.get(url=sheet_get_endopoint)
        pprint(response.json())








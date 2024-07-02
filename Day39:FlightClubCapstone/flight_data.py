import requests
import json



class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.url = 'https://api.sheety.co/yourapikey/flightDealsPrices/prices'
        self.response = requests.get(self.url)

        # if self.response.status_code == 200:
        #     self.data = self.response.json()
        #     print(self.data['prices'])
        # else:
        #     print(f"Failed to fetch data: {self.response.status_code}")

        self.data_flights = self.response.json()["prices"]

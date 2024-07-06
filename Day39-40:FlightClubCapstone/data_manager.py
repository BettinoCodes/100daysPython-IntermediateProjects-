import requests
import json


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    Attributes
    ----------
    URL : str
        The URL connected to the sheet.

    Methods
    -------
    show_excel(self):
        returns the information of the current sheet
    add_to_excel(self):
        allowing user to add a new row of information to the sheet
    add_testing(self):
        this add the IATA code to the current row based on the IATA
    
        
    """
    def __init__(self):
        self.url = 'https://api.sheety.co/00cf11bfb63c9d72833e19f6e988387d/flightDealsPrices/prices'

    def show_excel(self):
        response = requests.get(url=self.url)
        print(response.json())

    def add_to_excel(self):
        location_inp = input("Name a new location you want to go to: ")
        cheapest_price = input("What is the cheapest price so far? ")
        IATA_num = input("name a project IATA Code: ")
        body = {
            "price": {
                'city': location_inp,
                'lowestPrice': cheapest_price,
                'iataCode': IATA_num
            }
        }

        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url=self.url, headers=headers, data=json.dumps(body))
        print(response.text)
        print(response.status_code)

    def add_testing(self, i, value_str="TESTING"):
            url = f'https://api.sheety.co/00cf11bfb63c9d72833e19f6e988387d/flightDealsPrices/prices/{i}'
            body = {
                "price": {
                    'iataCode': value_str
                }
            }

            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.put(url=url, headers=headers, data=json.dumps(body))
            print(response.status_code)
            print(response.text)

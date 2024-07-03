import requests
import json


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = 'https://api.sheety.co/apikey/flightDealsPrices/prices'

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
            url = f'https://api.sheety.co/apikey/flightDealsPrices/prices/{i}'
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

    def add_test(self, value_str="TESTING"):
        for i in range(2, 11):
            url = f'https://api.sheety.co/apikey/flightDealsPrices/prices/{i}'
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


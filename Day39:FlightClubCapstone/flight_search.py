import requests
import datetime
from datetime import datetime as dt
from pprint import pprint

# from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = "key"
        self.api_secret = "secret"
        self.token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.flights_url = "https://test.api.amadeus.com/v1/security/oauth2/token/reference-data/locations/cities"
        self._token = self._get_new_token()
        self.location_prices_url = "https://test.api.amadeus.com/v2/shopping/flight-offers?"
    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=self.token_url, headers=header, data=body, verify=False)
        return response.json()['access_token']

    def get_iata(self, city_name):
        authorize = self._token
        print(f"authorize: {authorize}")
        city_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities?"

        headers = {
            "Authorization": f"Bearer {authorize}"
        }
        params = {
            "keyword": city_name,
            "max": 1
        }

        response = requests.get(url=city_url,params=params, headers=headers, verify=False)
        the_code = response.json()["data"][0]["iataCode"]
        return the_code

    def get_min_price_day(self, destination, depart_date, max_price):
        authorize = self._token
        dictionary_LP = []
        headers = {
            "Authorization": f"Bearer {authorize}"
        }
        params = {
            "originLocationCode": "NYC",
            "destinationLocationCode": destination,
            "departureDate": depart_date,
            "adults": 1,
            "nonStop": "false",
            "currencyCode": "USD",
            "maxPrice": max_price,
            "max": 5
        }

        response = requests.get(url=self.location_prices_url, params=params, headers=headers, verify=False)
        the_list_dict = response.json()["data"]
        # print(the_list_dict)

        min_grand_total = float('inf')
        min_flight_id = None
        min_departure_date = None

        # Loop through each offer to find the one with the minimum grandTotal
        for offer in the_list_dict:
            grand_total = float(offer['price']['grandTotal'])
            if grand_total < min_grand_total:
                min_grand_total = grand_total
                min_flight_id = offer['itineraries'][0]['segments'][0]['departure']['iataCode']
                min_departure_date = offer['itineraries'][0]['segments'][0]['departure']['at']

        return {
                "mingrand": min_grand_total,
                "Flight": min_flight_id,
                "Departure Date": min_departure_date,
                "To": destination
        }


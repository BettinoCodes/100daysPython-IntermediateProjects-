#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from notification_manager import NotificationManager
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import datetime

flight_data = FlightData()
data_manage = DataManager()
notify_manage = NotificationManager()
flight_search = FlightSearch()

# print(flight_data.data_flights)
last_row = flight_data.data_flights[len(flight_data.data_flights)-1]['id'] + 1
print(f"last: {last_row}")


#adding the IATA to the sheet
# for row_number in range(2, last_row): #last row
#     the_city_iata = flight_search.get_iata(flight_data.data_flights[row_number - 2]["city"])
#     data_manage.add_testing(row_number, value_str=the_city_iata)


date_now = datetime.datetime.now()
target_date = date_now + datetime.timedelta(days=5)
cop_date = datetime.datetime.now()
def get_lowest_price(list_prices):
    lowest = list_prices[0]["price"]
    for price in list_prices:
        if price["price"] < lowest:
            lowest = price["price"]
    return lowest

city_number = 0
all_prices_til_date = []
for city_number in range(len(flight_data.data_flights) - 5):
    iata_code = flight_data.data_flights[city_number]["iataCode"]
    cit = flight_data.data_flights[city_number]["city"]
    while date_now <= target_date:
        new_date = date_now.strftime("%Y-%m-%d")
        print(f"Loading... Current date: {new_date}")
        dict_of_data = flight_search.get_min_price_day(destination=iata_code, depart_date=new_date, max_price=flight_data.data_flights[city_number]["lowestPrice"])
        all_prices_til_date.append(dict_of_data)
        date_now += datetime.timedelta(days=1)
    date_now = datetime.datetime.now()
    city_number += 1

print(all_prices_til_date)







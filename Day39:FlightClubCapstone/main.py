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


def cheapest_depart_in_6_months_prices():
    global date_now, target_date
    all_prices_til_date = []
    for city_number in range(len(flight_data.data_flights) - 5):
        iata_code = flight_data.data_flights[city_number]["iataCode"]
        while date_now <= target_date:
            new_date = date_now.strftime("%Y-%m-%d")
            print(f"Loading... Current date: {new_date}")
            dict_of_data = flight_search.get_min_price_day(destination=iata_code, depart_date=new_date,
                                                           max_price=flight_data.data_flights[city_number][
                                                               "lowestPrice"])
            all_prices_til_date.append(dict_of_data)
            date_now += datetime.timedelta(days=1)
        date_now = datetime.datetime.now()
        city_number += 1

    return all_prices_til_date

def cheapest_by_day_each():
    for city_number in range(len(flight_data.data_flights)):
        iata_code = flight_data.data_flights[city_number]["iataCode"]
        print(f"Searching for {iata_code}...")
        lowest_price = flight_data.data_flights[city_number]["lowestPrice"]
        cheapest = flight_search.get_min_days(iata_code, depart_date=date_now, return_date=target_date, max_price=lowest_price)
        if cheapest == "None":
            print(f"No flights cheaper for {iata_code} on {date_now}")
        else:
            message_send = (f"WE FOUND CHEAPER FLIGHT TODAY FOR {iata_code}!\n"
                            f"Price: ${cheapest["mingrand"]}\n"
                            f"Airport: {cheapest["Flight"]}\n"
                            f"Departure Date: {cheapest["Departure Date"]}\n"
                            f"Return Date: {cheapest["Return Date"]}\n"
                            )
            notify_manage.send_notification(message_send)

def cheapest_by_day_each_email():
    list_messages = ""
    for city_number in range(len(flight_data.data_flights)):
        iata_code = flight_data.data_flights[city_number]["iataCode"]
        print(f"Searching for {iata_code}...")
        lowest_price = flight_data.data_flights[city_number]["lowestPrice"]
        cheapest = flight_search.get_min_days(iata_code, depart_date=date_now, return_date=target_date, max_price=lowest_price)
        if cheapest == "None":
            list_messages += f"No flights cheaper for {iata_code} on {date_now}\n"
        else:
            list_messages += (
                            f"WE FOUND CHEAPER FLIGHT TODAY FOR {iata_code}!\n"
                            f"Price: ${cheapest["mingrand"]}\n"
                            f"Airport: {cheapest["Flight"]}\n"
                            f"Departure Date: {cheapest["Departure Date"]}\n"
                            f"Return Date: {cheapest["Return Date"]}\n"
                        )
    return list_messages


#adding the IATA to the sheet
# for row_number in range(2, last_row): #last row
#     the_city_iata = flight_search.get_iata(flight_data.data_flights[row_number - 2]["city"])
#     data_manage.add_testing(row_number, value_str=the_city_iata)


date_now = datetime.datetime.now()
target_date = date_now + datetime.timedelta(days=30 * 6)
cop_date = datetime.datetime.now()

#for personal message to me
# cheapest_by_day_each()

# for emails in data sheet
for emails in data_manage.user_emails:
    message = cheapest_by_day_each_email()
    send_to = emails['whatEmailDoYouWantToUse?']
    print(send_to)
    notify_manage.send_email_notification(message=message, reciever=send_to)

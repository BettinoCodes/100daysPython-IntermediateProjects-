import requests
from twilio.rest import Client

account_sid = 'your id'
auth_token = 'your token'


url_weather = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key"

parameters = {
    "lat": your latitude,
    "lon": your longitude,
    "appid": api_key,
    "cnt":4
}
response = requests.get(url=url_weather, params=parameters)
print(response)
data = response.json()["list"]

for i in range(len(data)):
    place_id = data[i]["weather"][0]["id"]
    description = data[i]["weather"][0]["description"]
    if place_id < 700:
        print(place_id, description)
        print(type(place_id), type(description))
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+yourtwillionumber',
            body='You should know that it is going to rain today',
            to='whatsapp:+yournumber'
        )
        print(message.status)
        print(message.sid)
        break




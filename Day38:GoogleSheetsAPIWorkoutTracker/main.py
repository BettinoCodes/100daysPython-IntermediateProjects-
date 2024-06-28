import requests
from datetime import datetime as dt
import json
import os

weight_kg = "your weight"
height_cm = "your height"
age = "your age"

nutrition_id = "your id"
nutrition_api = "your api key"
nutrition_url = "your url"

url = "your url"
headers = {
    'Content-Type': 'application/json',
    'x-app-id': nutrition_id,
    'x-app-key': nutrition_api
}
data = {
    "query": input("What exercise did you do: "), #"Ran 2 miles and walked for 3Km"
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response_ex = requests.post(url, headers=headers, data=json.dumps(data))

exercises_data = response_ex.json()['exercises']

print(exercises_data)
print(len(exercises_data))

url = "your url"
response = requests.get(url)

date_now = dt.now()
time_now = date_now.time().strftime('%H:%M:%S')
day = date_now.strftime("%d/%m/%Y")

for i in range(len(exercises_data)):
    body = {
        "workout": {
                'date': day,
                'time': time_now,
                'exercise': exercises_data[i]['name'],
                'duration': exercises_data[i]['duration_min'],
                'calories': exercises_data[i]['nf_calories'],
        }
    }
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "your authorize key"
    }

    response_post = requests.post(url, headers=headers, data=json.dumps(body))
    print(f"here: {response_post.text}")

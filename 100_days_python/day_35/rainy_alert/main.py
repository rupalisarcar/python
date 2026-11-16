import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

LATITUDE = 3.342510
API_KEY = os.getenv("API_KEY")
print("APi = ", API_KEY)
LONGITUDE = 101.246803
parameters = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid" : API_KEY,
    "cnt":4
}

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?",params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]

# rainy_data = [item for item in weather_data if item["weather"]]
will_rain = False
for hourly_wetaher in weather_data:
    weather = (hourly_wetaher['weather'][0]['id'])
    print(weather)
    if weather < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Please bring an umbrella.",from_ ='+17372508034',
        to='+919051191115')
    print("Twilio connected successfully!")


print(weather_data)
# print(rainy_data)
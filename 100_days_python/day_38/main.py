import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT = 70                 #Optional: Weight in kg (1-500)
HEIGHT = 160                #Optional: Height in cm (1-300)
AGE = 33                    #Optional: Age (1-150)
# $env:BASIC_AUTH="Basic cnVwYWxpOlNhcmNhcjIwMjY="

APP_ID = os.environ["APP_ID"] 
API_KEY = os.environ["API_KEY"]

URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_URL = 'https://api.sheety.co/c0c82144e90f948873fee979fe37b7b1/workoutTracker/workouts'
AUTH = os.environ["BASIC_AUTH"]


headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_answer = input("Tell me which exercises you did : ")
data = {
    "query": user_answer,
    "weight_kg": WEIGHT,                  
    "height_cm": HEIGHT,                 
    "age": AGE,                       
    "gender": GENDER
}

response = requests.post(url=URL, json=data, headers=headers)
response.raise_for_status()

result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

auth_header = {
    "Authorization" : AUTH
}

for exercise in result["exercises"] : 
    sheet_inputs = {
        "workout": {
            "date" : today_date,
            "time" : today_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_URL, json=sheet_inputs, headers=auth_header)

    print(sheet_response)
    print(sheet_response.text)
 
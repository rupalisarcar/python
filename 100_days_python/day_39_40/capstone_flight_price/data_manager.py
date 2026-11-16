import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
PRICES_ENDPOINT = f"{os.environ["SHETTY_ENDPOINT"]}prices"
USERS_ENDPOINT = f"{os.environ["SHETTY_ENDPOINT"]}users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._username = os.environ["USERNAME"]
        self._password = os.environ["PASSWORD"]
        self._authorization = HTTPBasicAuth(self._username, self._password)
        self.destination_data = {}
        self.users = {}

    def get_destination_data(self) : 
        response = requests.get( url=PRICES_ENDPOINT, auth=self._authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_price(self, row_id, new_price):
        new_data = {
            "price":{
                "lowestPrice" : new_price
            }
        }

        response = requests.put(url=f"{PRICES_ENDPOINT}/{row_id}", json=new_data, auth=self._authorization)
        print("response " ,response)


    def get_customer_emails(self):
        user_response = requests.get( url=USERS_ENDPOINT, auth=self._authorization)
        user_response.raise_for_status()
        user_data = user_response.json()
        print("users data" , user_data)
        self.users = user_data['users']
        return self.users
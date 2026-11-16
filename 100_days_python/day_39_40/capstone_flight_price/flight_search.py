import os
from dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("SERP_API_KEY")

    def check_flights(self,origin_city_code, destination_city_code, from_date, to_date, is_direct):
        FLIGHT_SEARCH_BASE_URL = "https://serpapi.com/search"

        data_parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_date.strftime("%Y-%m-%d"),
            "return_date": to_date.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "INR",
            "api_key": self._api_key,
        }

        if is_direct:
            data_parameters["stops"] = "1"

        response = requests.get(url=FLIGHT_SEARCH_BASE_URL, params=data_parameters)
        response.raise_for_status()
        if response.status_code!=200:
            print(f"check_flights() response code: {response.status_code}")
            return None
        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
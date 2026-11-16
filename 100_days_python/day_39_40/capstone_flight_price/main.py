#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# requests_cache.install_cache(expire_after=3600, allowable_methods=('GET', 'POST'))

data_manager = DataManager()
destination_data = data_manager.get_destination_data()

users_data = data_manager.get_customer_emails()
user_email_list = [user['whatIsYourEmail'] for user in users_data] 

tommorrow = datetime.now() + timedelta(days=1)
six_month_from_today  = datetime.now() + timedelta(days=180)

flight_search = FlightSearch()
notification_manager = NotificationManager()

for data in destination_data:
    flights = flight_search.check_flights(origin_city_code = 'CCU', destination_city_code =data['iataCode'], from_date = tommorrow, to_date = six_month_from_today, is_direct=True)

    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))

    print(cheapest_flight.price)
    print(data['lowestPrice'])
    print(f"{data['city']}: INR {cheapest_flight.price}")

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight == "N/A" : 
        print(f"No direct flight to {data['city']}. Looking for indirect flights...")
        stopover_flights  = flight_search.check_flights(origin_city_code = 'CCU', destination_city_code =data['iataCode'], from_date = tommorrow, to_date = six_month_from_today, is_direct=False)
        
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: INR {cheapest_flight.price}")


    if cheapest_flight.price !="N/A" and cheapest_flight.price < data['lowestPrice']:
        data_manager.update_price(data["id"], cheapest_flight.price)
        if cheapest_flight.stops == 0:
            message =   f"Low price alert! Only INR {cheapest_flight.price} to fly direct "\
                        f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                        f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                    f"with {cheapest_flight.stops} stop(s) "\
                    f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        notification_manager.send_email(email_list=user_email_list, email_body=message)
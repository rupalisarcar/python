class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    all_flight = data.get("best_flights", []) +  data.get("other_flights", []) 

    first_flight = all_flight[0]
    lowest_price = first_flight["price"]
    origin  = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date  = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    print(origin)
    # A flight with 2 segments will have 1 stop
    nr_stops = len(first_flight["flights"]) - 1

    cheapest_flight = FlightData(price=lowest_price,origin_airport=origin, destination_airport=destination,out_date=out_date, return_date=return_date, stops=nr_stops)

    for flight in all_flight:
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            nr_stops = len(first_flight["flights"]) - 1
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    return cheapest_flight
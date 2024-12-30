import time
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()  # Fetch data from Sheety
flight_search = FlightSearch()

# Check for missing IATA codes and update them
for row in sheet_data:
    if row["iataCode"] == "YEAH":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

    # Push updated data back to Sheety
data_manager.destination_data = sheet_data
data_manager.update_destination_data()

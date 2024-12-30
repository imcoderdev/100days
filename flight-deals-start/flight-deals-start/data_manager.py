import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
SHEETY_USRERNAME="Namdev_sheet"
SHEETY_PASSWORD="random.randint"
SHEETDB_API_KEY="https://api.sheety.co/fbe5b551a4cd63aed63f5a3a6971e5fb/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.user=SHEETY_USRERNAME
        self.password=SHEETY_PASSWORD
        self._authorization=HTTPBasicAuth(self.user,self.password)
        self.destination_data={}
    def get_destination_data(self):
        response=requests.get(SHEETDB_API_KEY,auth=self._authorization)
        data=response.json()
        self.destination_data=data["prices"]
        pprint(self.destination_data)
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  # Match the key used in your database
                }
            }
            response = requests.put(
                url=f"{SHEETDB_API_KEY}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            response.raise_for_status()
            print(response.text)

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
SHEETY_USRERNAME="Namdev_sheet"
SHEETY_PASSWORD="random.randint"
SHEETDB_API_KEY="https://api.sheety.co/fbe5b551a4cd63aed63f5a3a6971e5fb/flightDeals/prices"
_authorization=HTTPBasicAuth(SHEETY_USRERNAME,SHEETY_PASSWORD)
response=requests.get(SHEETDB_API_KEY,auth=_authorization)
data=response.json()
data_prices=data["prices"]
# zero_data=data_prices[:]
for entry in data_prices:
    SHEETDB_PUT=f"{SHEETDB_API_KEY}/{entry['id']}"
    new_data = {
        "price": {
            "iataCode": entry["iataCode"]# Match the key used in your database
        }
    }

    new_data = {
        "price": {
            "iataCode": "TEST"
        }
    }
    response=requests.put(SHEETDB_PUT,json=new_data,auth=_authorization)
    print(response.text)
    new_data=entry["iataCode"]
    print(new_data)
# for city in response:



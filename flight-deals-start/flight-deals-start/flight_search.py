import requests
API_KEY="UYXQeoU3l9ve5NAR8Ai89A8owFJENZvT"
API_SECRET="GB1JkKejBV2L0Luz"
TOKEN_ENDPOINT="https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
class FlightSearch:
    def __init__(self):
        self.api_key=API_KEY
        self.api_secret=API_SECRET
        self.token=self._get_new_token()
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET

        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        print(response.json())
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
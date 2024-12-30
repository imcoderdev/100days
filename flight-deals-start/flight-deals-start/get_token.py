from http.client import responses

import requests
API_KEY="UYXQeoU3l9ve5NAR8Ai89A8owFJENZvT"
API_SECRET="GB1JkKejBV2L0Luz"
TOKEN_ENDPOINT="https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
city_name="Paris"
header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
body = {
    'grant_type': 'client_credentials',
    'client_id': API_KEY,
    'client_secret': API_SECRET

}
response=requests.post(url=TOKEN_ENDPOINT,headers=header,data=body)
API_TOKEN=response.json()["access_token"]
print(API_TOKEN)
headers = {"Authorization": f"Bearer {API_TOKEN}"}
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
response = requests.get(url=IATA_ENDPOINT, headers=headers,params=query)
print(response.json())
print(f"Status code {response.status_code}. Airport IATA: {response.text}")

import requests
import os
from twilio.rest import Client


account_sid = os.environ.get("sid")
auth_token = "1208d9366d68261f423828c6fd1a2d66"


url = "https://api.openweathermap.org/data/2.5/forecast"
api_id = os.environ.get("api_id_key")
parameters={
    "lat":19.997454,
    "lon":73.789803,
    "appid":api_id,
    "cnt":4,
}
request = requests.get(url,params=parameters)
weather_data=request.json()
will_rain= False
for hour_data in weather_data["list"]:
    weather_id=hour_data["weather"][0]["id"]
    if int(weather_id)<700:
        will_rain=True
if will_rain:
    print("bring umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Is is going to rain today so don't forget to bring Umbrella!",
        from_="+12316857844",
        to="+919067038936",
    )

    print(message.status)


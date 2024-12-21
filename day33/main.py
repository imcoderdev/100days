import time

import requests
from datetime import datetime
import smtplib
my_email = "kalenamdev168@gmail.com"
my_password = "fceeomaaeolnbfsa"


MY_LAT =20.000530
MY_LONG =73.782707
lower_lat = MY_LAT-5
upper_lat = MY_LAT+5
lower_long=MY_LONG-5
upper_long=MY_LONG+5
min_dark = 21
max_dark = 5
def check_iss():

        response = requests.get(url="http://api.open-notify.org/iss-now.json")


        response.raise_for_status()
        data = response.json()
        longitude = float(data["iss_position"]["longitude"])
        latitude = float(data["iss_position"]["latitude"])
        iss_location = (longitude, latitude)

        if lower_lat <= latitude <= upper_lat and lower_long <= longitude <= upper_long:
            return True





def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    now = datetime.now().hour
    if now>=sunset and now<=sunrise:
        return True



while True:
    time.sleep(60)

    if check_iss and is_dark:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:ISS is here\n\nIt's time to watch the ISS in the sky go fast"
            )














































import requests
from datetime import datetime
GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 177
AGE = 19
sheetdb_url="https://sheetdb.io/api/v1/ppjw9k25mwejh"
APP_ID="bb5ef448"
API_KEY="0e724350ecaa76b79546d141913108bd"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response=requests.post(url=exercise_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)
now = datetime.now()
today=now.strftime("%d/%m/%Y")
time=now.strftime("%H:%M:%S")
print(time)

for exercise in result["exercises"]:

    sheetdb_params={
        "workout":{
            "Date":today,
            "Time":time,
            "Exercise":exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"]
        }

    }
    sheetdb_response=requests.post(url=sheetdb_url,json=sheetdb_params)
    print(sheetdb_response.text)
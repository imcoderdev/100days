import requests

# API key for premium plans (if needed). Free-tier usage doesn't require this.
agify_api_key = "f426a5e52194ddbfad1e729434414e91"

def find(name):
    params = {"name": f"{name}"}
    agify_response = requests.get("https://api.agify.io", params=params)
    Agify_age= agify_response.json()["age"]
    genderize_response = requests.get("https://api.genderize.io", params=params)
    genderize_age= genderize_response.json()["gender"]
    print(Agify_age, genderize_age)
    return Agify_age,genderize_age,params
find(name="dev")

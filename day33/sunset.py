import requests
from datetime import datetime

MY_LAT = "56.619640"
MY_LNG = "-3.864780"

parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

this_hour = time_now.hour

if this_hour > sunrise and this_hour < sunset:
    print("The sun is out!")
else:
    print("The sun has set!")

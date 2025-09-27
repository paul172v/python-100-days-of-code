import requests
from dateutil.parser import parse
import smtplib, ssl
from email.message import EmailMessage
from email.utils import make_msgid, formatdate
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("WEATHER_API_KEY")

weather_params = {
    "lat": 56.619640,
    "lon": -3.864780,
    "appid": os.getenv("WEATHER_API_KEY"),
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=weather_params
)
response.raise_for_status()

weather_data = response.json()

weather_code = weather_data["list"][0]["weather"][0]["id"]

for i in range(0, 4):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        print(
            f"{parse(weather_data["list"][i]['dt_txt']).hour:02}:00 - Umbrella needed"
        )
        my_email = os.getenv("EMAIL")
        password = os.getenv("APP_PASSWORD")

        msg = EmailMessage()
        msg["Subject"] = "It's going to rain soon!"
        msg["From"] = my_email
        msg["To"] = "paul172v@yahoo.com"
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid()
        msg.set_content(
            f"{parse(weather_data["list"][i]['dt_txt']).hour:02}:00 - Umbrella needed"
        )

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.aol.com", 465, context=context, timeout=30) as smtp:
            smtp.set_debuglevel(1)
            smtp.login(my_email, password)
            smtp.send_message(msg)
    else:
        print(
            f"{parse(weather_data["list"][i]['dt_txt']).hour:02}:00 - Umbrella not needed"
        )


### Can use pythonanywhere to have a remote server that automatically executed .py files at specific times

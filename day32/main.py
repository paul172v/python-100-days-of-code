import pandas as pd
import random
import datetime as dt
import smtplib, ssl
from email.message import EmailMessage
from email.utils import make_msgid, formatdate
import os
from dotenv import load_dotenv

load_dotenv()

### Get today's month and year
now = dt.datetime.now()
this_month = now.month
this_day = now.day


data = pd.read_csv("./list.csv")
df = pd.DataFrame(data)


### Pick random letter
letters = ["letter1.txt", "letter2.txt", "letter3.txt"]
selected_letter = letters[random.randint(0, len(letters) - 1)]


### check if today matches the birthday of a listed person, and if so send email
for i in range(0, len(df)):

    ### Check if today is the birthday of a person on the list, if so send a birthday email
    if df.iloc[i]["month"] == this_month and df.iloc[i]["day"] == this_day:

        ### Open and replace [NAME] with the chosen person
        with open(f"./{selected_letter}", "r", encoding="utf-8") as f:
            message_arr = []

            ### Merge the birthday person with the chosen letter
            for line in f:
                line = line.replace("[NAME]", df.iloc[i]["name"])
                message_arr.append(line)

            ### Handle sending birthday email
            my_email = os.getenv("EMAIL")
            password = os.getenv("APP_PASSWORD")

            msg = EmailMessage()
            msg["Subject"] = "Happy Birth Day from Python"
            msg["From"] = my_email
            msg["To"] = "paul172v@yahoo.com"
            msg["Date"] = formatdate(localtime=True)
            msg["Message-ID"] = make_msgid()
            msg.set_content("\n".join(message_arr))

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(
                "smtp.aol.com", 465, context=context, timeout=30
            ) as smtp:
                smtp.set_debuglevel(1)
                smtp.login(my_email, password)
                smtp.send_message(msg)

            print("Sent via SSL 465")

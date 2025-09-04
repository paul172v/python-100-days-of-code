import smtplib, ssl
from email.message import EmailMessage
from email.utils import make_msgid, formatdate
import datetime as dt
import random


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 3:

    quotes = []

    with open("quotes.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if " - " in line:
                quote_text, author = line.rsplit(" - ", 1)
                quote_text = quote_text.strip().strip('"')
                author = author.strip()
                quotes.append((quote_text, author))

    random_quote_number = random.randint(0, 99)

    ####

    my_email = "paul172v@aol.com"
    password = "euqlsmblornyxyfg"

    msg = EmailMessage()
    msg["Subject"] = "Happy Quote Day from Python"
    msg["From"] = my_email
    msg["To"] = "paul172v@yahoo.com"
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid()
    msg.set_content(
        f"'{quotes[random_quote_number][0]}' - {quotes[random_quote_number][1]}"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.aol.com", 465, context=context, timeout=30) as smtp:
        smtp.set_debuglevel(1)
        smtp.login(my_email, password)
        smtp.send_message(msg)

    print("Sent via SSL 465")

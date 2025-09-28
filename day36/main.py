import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from twilio.rest import Client


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

### Task 1
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY}"
r = requests.get(stock_url)
stock_data = r.json()

today = datetime.today().date()
yesterday = today - timedelta(days=1)
ereyesterday = today - timedelta(days=2)

yesterday_stock = stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"]
ereyesterday_stock = stock_data["Time Series (Daily)"][f"{ereyesterday}"]["4. close"]

pct = round(
    (float(yesterday_stock) - float(ereyesterday_stock))
    / float(ereyesterday_stock)
    * 100,
    2,
)

### Task 2
news_url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={STOCK}&limit=3&apikey={API_KEY}"
r = requests.get(news_url)
news_data = r.json()

a1_title = news_data["feed"][0]["title"]
a1_summary = news_data["feed"][0]["summary"]

a2_title = news_data["feed"][1]["title"]
a2_summary = news_data["feed"][1]["summary"]

a3_title = news_data["feed"][2]["title"]
a3_summary = news_data["feed"][2]["summary"]

news = (
    f"{a1_title}\n{a1_summary}\n\n{a2_title}\n{a2_summary}\n\n{a3_title}\n{a3_summary}"
)

if float(yesterday_stock) >= (float(ereyesterday_stock) * 1.05):
    print(f"Up 5% or more\n\n{news}")

if float(yesterday_stock) <= (float(ereyesterday_stock) * 0.95):
    print(f"Down 5% or more, get news!\n\n{news}")

### Task 3
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

articles = [
    f"{a1_title}\n{a1_summary}",
    f"{a2_title}\n{a2_summary}",
    f"{a3_title}\n{a3_summary}",
]

# Send one SMS per article, each including the percent change header
if float(yesterday_stock) >= (float(ereyesterday_stock) * 1.05):
    for a in articles:
        sms_body = f"{STOCK}: 📈{pct}%\n\n{a}"
        client.messages.create(
            body=sms_body[
                :1500
            ],  # stay safely under SMS size; Twilio will segment as needed
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )

if float(yesterday_stock) <= (float(ereyesterday_stock) * 0.95):
    for a in articles:
        sms_body = f"{STOCK}: 📉{pct}%\n\n{a}"
        client.messages.create(
            body=sms_body[
                :1500
            ],  # stay safely under SMS size; Twilio will segment as needed
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )

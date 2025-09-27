import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

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


print(yesterday_stock, ereyesterday_stock)

if float(yesterday_stock) >= (float(ereyesterday_stock) * 1.05):
    print("Up 5% or more")

if float(yesterday_stock) <= (float(ereyesterday_stock) * 0.95):
    print("Down 5% or more, get news!")


### Daily limit, 25 per day!!!!

# ### Task 2
# news_url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={STOCK}&limit=3&apikey={API_KEY}"
# r = requests.get(news_url)
# news_data = r.json()

# print(news_data)

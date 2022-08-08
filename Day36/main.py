import html

import requests
from function import will_get_news, cleanhtml, get_msg_content


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# parameters for API
stock_API_endpoint = "https://www.alphavantage.co/query"
stock_API_params = {"apikey": "YOWVC60ODLDNOWK0",
          "function": "TIME_SERIES_DAILY",
          "symbol": STOCK}

stock_data = requests.get(url=stock_API_endpoint, params=stock_API_params)
stock_data.raise_for_status()

# extract closing price from yesterday and the day before
daily_data = stock_data.json()["Time Series (Daily)"]
data_date = list(daily_data.keys())
yesterday = daily_data[data_date[0]]
day_before = daily_data[data_date[1]]

# whether will get news base on closing stock price
percent_diff = will_get_news(yesterday, day_before)
percent_diff = round(percent_diff, 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_API_endpoint = "https://newsapi.org/v2/everything"
news_API_key = "4e2fa9fa36264d0a83820c3bc0ab85a4"
news_API_params = {"q": "Tesla+stock",
                   "from": yesterday,
                   "to": day_before,
                   "sortBy": "popularity",
                   "searchIn": "title",
                   "language": "en",
                   "apiKey": news_API_key}

news_data = requests.get(url=news_API_endpoint, params=news_API_params)
headline = news_data.json()["articles"][0]["title"]
brief = news_data.json()["articles"][0]["description"]
brief = html.unescape(brief)
brief = cleanhtml(brief)
msg_content = get_msg_content(percent_diff, headline, brief)
print(msg_content)




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
from datetime import datetime as dt
from twilio.rest import Client
from data_stocks import data

STOCK = "stockofcompany"
COMPANY_NAME = "a company"

news_api = "yournewsapikey"
stock_api = "yourstockapikey"

account_sid = 'youraccountid'
auth_token = 'yourauthtoken'

# STEP 1: Use https://www.alphavantage.co
#When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params=parameters)
data_stocks = r.json()

now = dt.now()
print(now.date())


dict_of_dates = data_stocks["Time Series (Daily)"].items()

last_two_days = first_two_items = list(dict_of_dates)[1:3]

yesterday_close = float(last_two_days[0][1]['4. close'])
day_bfr_yesterday_close = float(last_two_days[1][1]['4. close'])

percentage_change = round(((yesterday_close - day_bfr_yesterday_close) / day_bfr_yesterday_close) * 100, 2)

# Determine if it's at least a 5% increase or decrease
if percentage_change >= 5 or percentage_change <= -5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    url_news = (
        'https://newsapi.org/v2/everything?'
        'q=Tesla&'
        'from=2024-06-26&' 
        'language=en&'
        'sortBy=popularity&' #publishedAt
        'apiKey=yourapikey'
    )
    response = requests.get(url_news)
    news_data = response.json()

    links_to_news = []
    for i in range(3):
        links_to_news.append(news_data["articles"][i])

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    message_send = ""

    if percentage_change >= 5:
        message_send = f'{STOCK}: 🔺{percentage_change}\n'
    elif percentage_change <= -5:
        message_send = f'{STOCK}: 🔻{percentage_change}\n'

    for i in range(len(links_to_news)):
        message_send += (f'Article {i+1}\n'
                         f'Title: {links_to_news[i]["title"]}\n'
                         f'Description: {links_to_news[i]["description"]}\n'
                         f'Link:{links_to_news[i]["url"]}\n'
                         )

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+twillionumber',
        body=f'{message_send}',
        to='whatsapp:+yournumber'
    )
    print(message.status)
    print(message.sid)

else:
    print("No significant change (less than 5%)")



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



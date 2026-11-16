import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_END_POINT = "https://www.alphavantage.co/query"
NEWS_END_POINT = "https://newsapi.org/v2/everything"
API_KEY = "617OEX7O40J0RP01"
NEWS_API_KEY = "6519a198a45448a190c0851251facac8"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
param = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : API_KEY
}
response = requests.get(STOCK_END_POINT,params=param)
response.raise_for_status()
data=response.json()
print(data)
# # ['Time Series (Daily)']
# new_data = [value for (key, value) in data.items()]

# yesterday_data = new_data[0]['4. close']
# before_yesterday_data = new_data[1]['4. close']

# differnce_data = abs(float(yesterday_data) - float(before_yesterday_data))
# differnce_data_percentage = (differnce_data/ float(yesterday_data))*100

# if differnce_data_percentage >4:
#     print("Get News")
#     parameter = {
#         "apiKey" : NEWS_API_KEY,
#         "q":COMPANY_NAME
#     }
#     response_news = requests.get(NEWS_END_POINT,params=parameter) 
#     response_news.raise_for_status()
#     news_data = response_news.json()
    
#     print(news_data)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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


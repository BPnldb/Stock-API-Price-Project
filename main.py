import requests


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "D0MXDR14EH3KO9RZ"
NEWS_API_KEY = "79e78876acfb41e1a7c6829948592f4b"



def stocks_difference():
    #yesterady
    data_list = [value for (key, value) in data.items()] #prints the value of the key(price)
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    print(f"Yesterday's closing price ${'%.2f' % float(yesterday_closing_price)}")

    # day before yesterday
    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print(f"Day before yesterday's closing price: ${'%.2f' % float(day_before_yesterday_closing_price)}")

    up_down = None
    if yesterday_closing_price > day_before_yesterday_closing_price:
        up_down = "🔺"
    else:
        up_down = "🔻"

    #difference between the two days
    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
    print(f'Difference: ${"%.2f" % difference} {up_down}')

    diff_percent = ((difference / float(day_before_yesterday_closing_price)) * 100)
    print(f'Percent: {round(diff_percent, 2)}% {up_down}')

    # news API
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #formatting
    for a in range(0, len(articles) // 4):
        print(f'{a + 1}. Title: {articles[a]["title"]}')
        print(f' Description: {articles[a]["description"]}')
        print(f' {articles[a]["url"]}\n')


while True:
    STOCK_NAME = input("Enter the company stock name: ")
    COMPANY_NAME = input("Enter the company name: ")

    # stock name
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    try:
        response = requests.get(STOCK_ENDPOINT, params=stock_params)
        data = response.json()["Time Series (Daily)"]
    except KeyError:
        #while KeyError:
        print("Wrong stock name")
        STOCK_NAME = input("Enter the company stock name: ")

        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": STOCK_API_KEY,
        }
        response = requests.get(STOCK_ENDPOINT, params=stock_params)
        data = response.json()["Time Series (Daily)"]
    stocks_difference()
    entry = input("Continue search?").lower()
    if entry == 'no':
        print("Exiting stock app")
        break










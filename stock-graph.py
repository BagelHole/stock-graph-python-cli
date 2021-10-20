# Simple stock graph script
import datetime
from dateutil.relativedelta import relativedelta
from tiingo import TiingoClient
import matplotlib.pyplot as plt
from matplotlib import style

all_tickers = []
n = 0
k = 0
dates_string = ""
tickers_string = ""
legend_string = ""
one_year_ago = datetime.datetime.now() - relativedelta(years=1)
six_months_ago = datetime.datetime.now() - relativedelta(months=6)
one_month_ago = datetime.datetime.now() - relativedelta(months=1)

style.use("fivethirtyeight") # matlab style

config = {}  # config for the TiingoClient and API
config['session'] = True
config['api_key'] = 'your_key' # Add your own api key for tiingo https://api.tiingo.com/
client = TiingoClient(config) # setting client equal to the TiingoClient with the api key in config

start = six_months_ago
end = datetime.datetime.now()

if start == six_months_ago:
    dates_string = "Six Months"
elif start == one_year_ago:
    dates_string = "One Year"
elif start == one_month_ago:
    dates_string = "One Month"

while True:

    while True:
        try:
            print("Type 'Exit' to leave.")
            ticker = input("What Ticker would you like?: ")

            ticker = ticker.upper()

            all_tickers.append(ticker)

            if ticker == "EXIT":
                break
    
            stock_data = client.get_dataframe(ticker,frequency = 'daily', startDate = start, endDate = end) # setting dataframe with ticker, frequency, dates
            break

        except:
            print("Please use a valid Ticker.")
            all_tickers.pop(n)
            continue
    
    if ticker == "EXIT":
                break

    print("\n",ticker,"Data\n",stock_data) 

    tickers_string = ", ".join(all_tickers) 

    print(tickers_string)

    stock_data["high"].plot(label=ticker) # Matlab plotting of graph and showing
    plt.title(tickers_string+" Stock Performance Over "+dates_string)
    plt.legend()
    plt.draw()
    plt.show(block = False)

    n = n +1

    continue
	

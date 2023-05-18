stocks = { "AAPL" : 168.68, "MSFT" : 307.26, "GOOGL" : 107.34, "AMZN" : 105.45, "TSLA" : 164.31 , \
            "INTC" : 31.06, "CSCO" : 47.25, "AMD" : 89.37, "FB" : 240.32 , "NFLX" : 329.93}
            
ticker = input('Enter a ticker symbol (e.g. GOOGL). Type QUIT to stop: ')
while not ticker == "QUIT":
    if ticker in stocks:
        print('{} : {}'.format(ticker, stocks[ticker]))
    else:
        print('{} not found'.format(ticker))

    ticker = input('Enter a ticker symbol (e.g. GOOGL). Type QUIT to stop: ')
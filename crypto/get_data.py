import ccxt

def get_historical_prices(exchange, market, time_frame):
     
     """
     return historical prices(trades) of particular market 
     
     exchange - string -  exchange name (https://github.com/ccxt/ccxt/wiki/Exchange-Markets) 
     market - string  - market name (example "BTC/USD")
     time_frame - string ('5m','15min' ... )
     """
    
    # create exchange
    exchange = getattr(ccxt, exchange)()
    # get historical trades
    try:
        result = exchange.fetch_ohlcv(market, time_frame)
    except Exception as err:
        print(err)
        return None
    return result
    




def get_intraday_history(ticker, time_frame):
    """

    get intraday historical prices
    https://www.alphavantage.co/documentation/

    :param ticker:  string. "AAPL", "AMZN" ...
    :param time_frame: string. "1m","15m"
    :return: pandas dataframe
    """

    api_key = '' # API key from https://www.alphavantage.co

    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker, interval = time_frame, outputsize = 'full')
    return data


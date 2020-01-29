
import pandas as pd


def create_df(data):
    
    """
    convert historical trades data to DataFrame table
    
    data: array of arrays with columns 'time', 'open', 'high', 'low', 'close', 'volume'
          
          example:
          "
          [[1580179500000, 9107.0, 9125.61, 9101.99, 9122.68, 144.41624],
          [1580179800000, 9122.68, 9131.83, 9121.72, 9122.84, 96.803208],
          ...
          [1580180400000, 9119.74, 9122.0, 9108.85, 9109.31, 94.420047]]
          
         "

    """


    # create pandas DateFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame.from_records(data, columns=columns, index = 'time')
    # convert timestamp to UTC datetime
    df.index = pd.to_datetime(df.index / 1000, unit = 's').tz_localize(tz='GMT')
    # convert UTC to San Francisco
    df = df.tz_convert(tz='America/Los_Angeles')
    # sort by date (last candle is first)
    df = df.sort_index(axis=0, ascending=False)

    return df

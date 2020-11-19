# Strategies for trading

# Import necessary libraries
import pandas as pd
from stockstats import StockDataFrame as Sdf

def test_macd_strategy(stock_df, stock_symbol):
    ''' Tests MACD Strategy
    Args:
        stock_df (df): Asset dataframe containing ticker symbol key and
        column headings: 'open', 'close', 'high', 'low', and 'volume'.
    Returns:
        BUY, SELL, or HOLD string signal
    '''

    # Sort columns for stockdataframe
    data = stock_df[stock_symbol][['open', 'close', 'high', 'low', 'volume']]

    # Change from pandas dataframe to stockdataframe
    stock  = Sdf.retype(data)

    # Signal line
    signal = stock['macds']

    # The MACD that needs to cross the signal line to give you a Buy/Sell signal
    macd   = stock['macd']

    for i in range(1, len(signal)):
        # If the MACD crosses the signal line upward
        if macd[i] > signal[i] and macd[i - 1] <= signal[i - 1]:
            return 'BUY'
        # The other way around
        elif macd[i] < signal[i] and macd[i - 1] >= signal[i - 1]:
            return 'SELL'
        # Do nothing if not crossed
        else:
            return 'HOLD'

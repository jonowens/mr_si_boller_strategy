# This is a program to trade using Bollinger Bands to pay the bills

# Import necessary libraries
import pandas as pd
from libs import connections, strategies

# Instantiate variables
ticker_symbol = 'GOOG'
timeframe = '1D'
num_intervals = 1000
starting_date = '2020-11-15'
ending_date = '2020-11-16'

# Setup connection to Alpaca
trader = connections.alpaca_trading_connection()

# Get ticker data
stock_df = trader.get_asset_history(ticker_symbol, timeframe, num_intervals, starting_date, ending_date).df

# Check bollinger band strategy indicator
response = strategies.test_macd_strategy(stock_df, ticker_symbol)
print(response)
# Check macd strategy indicator

# Check rsi strategy indicator

# If all three indicators are equal to buy
    # place buy order with OCO (2% market close order (profit) and 1% market close order (loss))

# else if all three indicators are equal to sell
    # place sell market close order

# else do nothing

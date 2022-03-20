import pandas as pd
import urllib.request

# Read from h5
df = pd.read_hdf('hdfstore.h5', 'd1')
print(df.head())

# # Create JSON
# df.to_json('example_json.json')

# Read JSON
df2 = pd.read_json('example_json.json')
print(df2.head())

# Request to read from Giphy Public API - Trending
get_market_history_json = urllib.request.urlopen(
    'https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=USD-BTC').read()

print(get_market_history_json)

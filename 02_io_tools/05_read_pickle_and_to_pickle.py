import pandas as pd
import urllib.request
import pickle
import time

get_market_history = urllib.request.urlopen(
    'https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=USD-BTC')

df = pd.read_json(get_market_history)

df.to_pickle('pickle.pickle')
new_df = pd.read_pickle('pickle.pickle')

# Write JSON string to Pickle --> write binary
pickle_out = open('newdf.pickle', 'wb')
pickle.dump(new_df, pickle_out)
pickle_out.close()

# Read Pickle file --> read binary
pickle_in = open('newdf.pickle', 'rb')
super_cool = pickle.load(pickle_in)

print(super_cool)
print(super_cool.head())

start = time.time()
df.to_pickle('pickle.pickle')
new_df = pd.read_pickle('pickle.pickle')
print(time.time() - start)

start = time.time()
pickle_out = open('newdf.pickle', 'wb')
pickle.dump(new_df, pickle_out)
pickle_out.close()
pickle_in = open('newdf.pickle', 'rb')
super_cool = pickle.load(pickle_in)

print(time.time() - start)

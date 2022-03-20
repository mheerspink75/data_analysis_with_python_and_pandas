import pandas as pd
import sqlite3
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
# from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

def populate_DB():
    chunks = pd.read_csv('./06_advanced_operations/btceUSD.csv', chunksize=10000)
    for chunk in chunks:
        chunk.columns = ['Unix', 'Price', 'Volume']
        with sqlite3.connect('./07_working_with_databases/tutorial.db') as conn:
            chunk.to_sql('Bitcoin', conn, if_exists='append')


# populate_DB()

def pull_from_DB():
    with sqlite3.connect('./07_working_with_databases/tutorial.db') as conn:
        df = pd.read_sql('SELECT * FROM Bitcoin LIMIT 10000', con=conn, index_col='index')
    return df

df = pull_from_DB()
# print(df.head())

df['Date'] = pd.to_datetime(df['Unix'], unit='s')
df.set_index('Date', inplace=True)
del(df['Unix'])

print(df.head())

ohlc = df['Price'].resample('1D').ohlc()

print(ohlc.head())

#ohlc['']

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
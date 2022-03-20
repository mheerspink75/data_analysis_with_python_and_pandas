import pandas as pd
import urllib.request
import matplotlib.pyplot as plt


def pickle_data():
    read = urllib.request.urlopen(
        'https://www.quandl.com/api/v3/datasets/NASDAQOMX/NDX.csv?api_key=ex2pky69KhUKeLvuWYSN')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df.pickle')


pickle_data()

df = pd.read_pickle('df.pickle')
df.sort_values('Trade Date', inplace=True)
df.set_index('Trade Date', inplace=True)
df = df['High']
print(df.head())

df.plot()
plt.show()

df = pd.read_pickle('df.pickle')
print(df.head())
df.sort_values('Low', inplace=True)
print(df.head())

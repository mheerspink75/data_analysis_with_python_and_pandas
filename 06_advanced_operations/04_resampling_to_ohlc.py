import pandas as pd

df = pd.read_pickle('df.pickle')
df.sort_values('Trade Date', inplace=True)

df['Trade Date'] = pd.to_datetime(df['Trade Date'])
df.set_index('Trade Date', inplace=True)

print(df.head())

# ohlc = open, high, low, close
df2 = df['Index Value'].resample('2D').ohlc()
print(df2.head())

if df2.isnull().values.sum() > 1:
    print('We contain NAN data!')

df2.dropna(inplace=True)
print(df2.head())

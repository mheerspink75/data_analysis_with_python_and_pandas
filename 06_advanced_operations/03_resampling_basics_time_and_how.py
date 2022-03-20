import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('fivethirtyeight')

df = pd.read_pickle('df.pickle')
df.sort_values('Trade Date', inplace=True)

df['Trade Date'] = pd.to_datetime(df['Trade Date'])
df.set_index('Trade Date', inplace=True)

print(df.head())

# 3D = 3day offset alias
df2 = df.resample('3D').mean()
print(df2.head())

df3 = df.resample('3D').mean()
print(df3.head())

df4 = df.resample('3D').mean()
print(df4.head())

df2['Index Value'].plot()
df3['Index Value'].plot()
df4['Index Value'].plot()
df['Index Value'].plot()

plt.show()

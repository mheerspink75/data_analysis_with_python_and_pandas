import datetime
import pandas_datareader.data as web

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2000, 10, 15)
end = datetime.datetime(2019, 10, 20)

att = web.DataReader('T', 'yahoo', start, end)

print(att.head())

# att['Adj Close'].plot()
att['High'].plot()
att['Low'].plot()

# Plot high and low to graph
att[['High', 'Low']].plot()
plt.legend()
plt.show()

# Plot the entire dataframe
att.plot()
plt.legend()
plt.show()

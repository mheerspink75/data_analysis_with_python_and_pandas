import pandas as pd
import pandas_datareader.data as web
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2019, 10, 23)

att = web.DataReader("T", 'yahoo', start, end)

print(att.head())
print(50*"#")

att['Open_original'] = att['Open']
att['Open'] = att['Open'] / 10

print(att.tail())

att['High_minus_low'] = att['High'] - att['Low']

print(att.tail())

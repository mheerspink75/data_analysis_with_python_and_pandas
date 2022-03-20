import datetime
import pandas_datareader.data as web

start = datetime.datetime(2000, 10, 15)
end = datetime.datetime(2019, 10, 20)

att = web.DataReader('T', 'yahoo', start, end)

print(att.tail())

# Convert to list
highs = att['High'].tolist()

print(highs)

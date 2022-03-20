import pandas_datareader.data as web
import datetime

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2019, 10, 23)

att = web.DataReader("T", 'yahoo', start, end)

print(att.head())
print(50 * "#")

describe = att.describe()

print(att.describe)
print(describe['Open'])
print(describe['Open']['std'])

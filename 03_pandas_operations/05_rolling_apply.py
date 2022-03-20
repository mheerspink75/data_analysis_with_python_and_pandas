import pandas_datareader.data as web
from matplotlib import style
from statistics import mean
import datetime


def moving_average(data):
    return mean(data)


def fancy_this(data):
    return mean(data) + mean(data) + 5


style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2019, 10, 23)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
print(describe['Open']['std'])

att['50MA'] = att['Close'].rolling(50).mean()
att['10MA'] = att['Close'].rolling(10).mean()
att['50STD'] = att['Close'].rolling(50).std()

att['MA_with_apply'] = moving_average(att['Close'].rolling(50).mean())
att['apply'] = fancy_this(att['Close'].rolling(50).mean())

print(att.tail())

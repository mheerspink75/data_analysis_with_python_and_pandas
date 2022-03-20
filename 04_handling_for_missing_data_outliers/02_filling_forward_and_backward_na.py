import pandas_datareader.data as web
from matplotlib import style
import datetime

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2019, 10, 23)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
print(describe['Open']['std'])

att['50MA'] = att['Close'].rolling(50).mean()
att['10MA'] = att['Close'].rolling(10).mean()
att['50STD'] = att['Close'].rolling(50).std()
print(att.head())

one_pct = int(len(att) * 0.01)

att.fillna(value=-99999, inplace=True, limit=one_pct)
print(att)

if att.isnull().values.sum() > 1:
    print('Found remaining NA, more than 1% is not a number')

att.fillna(value=-99999, inplace=True, limit=9000)

if att.isnull().values.sum() > 1:
    print('Found remaining NA, more than 1%+9000 is not a number')

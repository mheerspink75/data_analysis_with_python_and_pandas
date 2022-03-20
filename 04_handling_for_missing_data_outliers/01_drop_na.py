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

# Drop NA Columns
att1 = att.dropna(axis=1)
print(att1.head())

# Drop NA Rows
att2 = att.dropna(axis=0)
print(att2.head())

# If values are NA, drop that row or column
att3 = att.dropna(how='all')
print(att3.head())

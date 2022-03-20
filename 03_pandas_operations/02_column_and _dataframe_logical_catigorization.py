import pandas_datareader.data as web
import datetime

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2019, 10, 23)

att = web.DataReader("T", 'yahoo', start, end)

print(att.tail())
print(50 * "#")

att['Daily_Rise'] = att['Close'] > att['Open']
print(att.tail())

att2 = att[(att['Close'] > att['Open'])]
print(att2.tail())

att['HL'] = att['High'] - att['Low']
att3 = att[(att['HL'] > 1)]
print(att3.tail())

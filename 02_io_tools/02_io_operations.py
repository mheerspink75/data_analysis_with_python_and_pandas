import pandas as pd

# CSV, Russian Federation Statistics Service - Recorded Crimes, Quandl.com
df = pd.read_csv('RFSS-OFCRIMES.csv')

# Set dataframe index to 'Date"
df = df.set_index('Date')
df['Crimes recorded - total'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df)

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

# Read dataframe newcsv2.csv and name column headers
df = pd.read_csv('newcsv2.csv', names=['Date', 'Total_Crimes_Recorded'], index_col=0)
print(df.head())

# Create new csv with column headers
df.to_csv('newcsv3.csv')

# Create new csv with no headers
df.to_csv('newcsv4.csv', header=False)

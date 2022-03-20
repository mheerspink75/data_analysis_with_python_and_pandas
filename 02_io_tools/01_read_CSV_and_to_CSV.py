import pandas as pd

# CSV, Russian Federation Statistics Service - Recorded Crimes, Quandl.com
df = pd.read_csv('RFSS-OFCRIMES.csv')

# Converts dataframe to new CSV file
df.to_csv('newcsv.csv')

# Converts 'Crimes recorded - total' to new CSV file
df['Crimes recorded - total'].to_csv('newcsv2.csv')
print(df)

# Set dataframe index to 'Date"
df = df.set_index('Date')
df['Crimes recorded - total'].to_csv('newcsv2.csv')
print(df)

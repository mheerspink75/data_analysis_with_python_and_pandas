import pandas as pd

# Read from CSV
df = pd.read_csv('newcsv4.csv',
                 names=['Date', 'Total_Crimes_Recorded'], index_col=0)
print(df.head())

# Create hdfstore.h5 file
store = pd.HDFStore('hdfstore.h5')
print(store)

# Format h5
store.put('d1', df, format='table', data_columns=True)

print(store['d1'].shape)
store.close()

# Read h5
hdf = pd.read_hdf('hdfstore.h5', 'd1')
print(hdf)

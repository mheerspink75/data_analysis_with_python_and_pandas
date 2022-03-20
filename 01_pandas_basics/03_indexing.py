import pandas as pd

starting = {
    'Col_1': [5, 2, 4, 7, 2, 4],
    'Col_2': [7, 8, 2, 1, 5, 6],
    'Col_3': [10, 4, 2, 1, 8, 2],
    'Name': ['HG', 'TY', 'CS', 'YU', 'PO', 'XW'],
    'Col_4': [5, 6, 7, 1, 1, 4],
    'Col_5': [9, 9, 2, 1, 5, 2],
    'Col_6': [7, 8, 2, 1, 7, 8],
}

df = pd.DataFrame(starting)

# print the index
print(df.index)

# set the index
df = df.set_index('Name')

# print the index
print(df.index)

# check the dataframe
print(df.head())

import pandas as pd

school = {
    'Name': ['Jeff', 'Carrol', 'Kyle', 'Adrian', 'Jessica', 'Scott', 'Tanner', 'Kelly', 'Brittney', 'Joe'],
    'Age': [18, 17, 15, 15, 16, 17, 18, 19, 18, 14],
    'Grade': [12, 11, 9, 10, 11, 12, 12, 11, 10, 9],
}

df = pd.DataFrame(school)
print(df)

df2 = df.sort_values('Grade')
print(df2)

df3 = df.sort_values(['Grade', 'Age'])
print(df3)

df4 = df.sort_values(['Grade', 'Age', 'Name'])
print(df4)

df5 = df.sort_values(['Grade', 'Age', 'Name'], ascending=False)
print(df5)

df6 = df.sort_values(['Grade', 'Age', 'Name'], ascending=[False, True, True])
print(df6)

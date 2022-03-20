import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('fivethirtyeight')


def pct_diff(v1, v2):
    pct = ((v2 - v1) / v1) * 100.0
    return pct


df = pd.read_pickle('df3.pickle')
df.set_index('Quarter', inplace=True)
df.sort_index(inplace=True)
print(df.head())

df['Pct_Diff_NGDP1_vs_NGDP5'] = list(map(pct_diff, df['NGDP1'], df['NGDP2']))

df['Pct_Diff_NGDP1_vs_NGDP2_again'] = ((df['NGDP2'] - df['NGDP1']) / df['NGDP1']) * 100
print(df.head())

df['Pct_Diff_NGDP2_vs_NGDP5'] = list(map(pct_diff, df['NGDP2'], df['NGDP5']))
df['Pct_Diff_NGDP3_vs_NGDP5'] = list(map(pct_diff, df['NGDP3'], df['NGDP5']))
df['Pct_Diff_NGDP4_vs_NGDP5'] = list(map(pct_diff, df['NGDP4'], df['NGDP5']))

df['Pct_Diff_NGDP1_vs_NGDP5'].plot(label='NGDP1')
df['Pct_Diff_NGDP2_vs_NGDP5'].plot(label='NGDP2')
df['Pct_Diff_NGDP3_vs_NGDP5'].plot(label='NGDP3')
df['Pct_Diff_NGDP4_vs_NGDP5'].plot(label='NGDP4')
plt.legend(loc=4)
plt.show()

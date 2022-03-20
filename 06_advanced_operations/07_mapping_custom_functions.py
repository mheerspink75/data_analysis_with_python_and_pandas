import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


def pct_diff(v1, v2):
    pct = ((v2 - v1) / v1) * 100.0
    return pct


df = pd.read_pickle('df3.pickle')
df.set_index('Quarter', inplace=True)
df.sort_index(inplace=True)
print(df.head())

df['Pct_NGDP1_vs_NGDP2'] = list(map(pct_diff, df['NGDP1'], df['NGDP2']))
df['Pct_NGDP1_vs_NGDP2'].plot()
plt.show()

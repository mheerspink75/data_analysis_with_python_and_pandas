import pandas as pd
import urllib.request


def pickle_data():
    read = urllib.request.urlopen(
        'https://www.quandl.com/api/v3/datasets/RFSS/OFCRIMES.csv?api_key=ex2pky69KhUKeLvuWYSN')
    df1 = pd.read_csv(read)
    print(df1.head())
    df1.to_pickle('./06_advanced_operations/df1.pickle')

    read = urllib.request.urlopen(
        'https://www.quandl.com/api/v3/datasets/FED/STFBAILSS_XQA_XDO_MA_N_Q.csv?api_key=ex2pky69KhUKeLvuWYSN')
    df2 = pd.read_csv(read)
    print(df2.head())
    df2.to_pickle('./06_advanced_operations/df2.pickle')

    read = urllib.request.urlopen(
        'https://www.quandl.com/api/v3/datasets/FRBP/NGDP_MD.csv?api_key=ex2pky69KhUKeLvuWYSN')
    df3 = pd.read_csv(read)
    print(df3.head())
    df3.to_pickle('./06_advanced_operations/df3.pickle')

    read = urllib.request.urlopen(
        'https://www.quandl.com/api/v3/datasets/JODI/OIL_CRIMKD_USA.csv?api_key=ex2pky69KhUKeLvuWYSN')
    df4 = pd.read_csv(read)
    print(df4.head())
    df4.to_pickle('./06_advanced_operations/df4.pickle')


# pickle_data()

df1 = pd.read_pickle('df1.pickle')
df2 = pd.read_pickle('df2.pickle')
df3 = pd.read_pickle('df3.pickle')
df4 = pd.read_pickle('df4.pickle')

print(df3.corr())

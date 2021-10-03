import pandas as pd

df01 = pd.read_csv("df_basic.csv")
# print(df01)
df01.head()
# print(df01.head())

df02 = pd.read_csv("df_trade.csv")
# print(df02)
df = pd.merge(df01, df02, on='id')
# print(df)
d = df.drop(['gender', 'edu', 'age'], axis=1)
print(d)
dd = d[d['is_vip'] == 1]
print(dd)

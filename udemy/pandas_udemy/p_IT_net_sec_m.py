import pandas as pd

df1 = "/Users/a/pandas_udemy/p_IT_net_sec.csv"
df2 = "/Users/a/pandas_udemy/p_IT_net_sec3.csv"


p_IT_net_sec_m = pd.concat(
   map(pd.read_csv, [df1, df2]), ignore_index=True)

p_IT_net_sec_m.to_csv("p_IT_net_sec_m.csv", index=False)
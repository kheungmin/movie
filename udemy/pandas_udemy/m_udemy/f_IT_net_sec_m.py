import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_IT_net_sec_m.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("IT_net_security")

df.to_csv("p_IT_net_sec_m.csv", index=False)
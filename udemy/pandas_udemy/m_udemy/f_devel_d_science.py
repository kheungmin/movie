import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_d_science.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("data_science")

df.to_csv("p_devel_d_science.csv", index=False)
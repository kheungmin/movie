import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_DB.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("DataBase")

df.to_csv("p_devel_DB.csv", index=False)
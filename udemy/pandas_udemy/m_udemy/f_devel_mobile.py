import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_mobile.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("devel_mobile")

df.to_csv("p_devel_mobile.csv", index=False)
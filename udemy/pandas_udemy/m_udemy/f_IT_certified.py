import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_IT_certified.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("IT_certified")

df.to_csv("p_IT_certified.csv", index=False)
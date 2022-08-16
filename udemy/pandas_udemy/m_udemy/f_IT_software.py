import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_IT_software.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("IT_software")

df.to_csv("p_IT_software.csv", index=False)
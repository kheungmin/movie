import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_IT_hardware.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("IT_hardware")

df.to_csv("p_IT_hardware.csv", index=False)
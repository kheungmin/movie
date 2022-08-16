import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_software_eg.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("software_engineering")

df.to_csv("p_devel_software_eg.csv", index=False)
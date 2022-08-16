import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_software_tool.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("software_tool")

df.to_csv("p_devel_software_tool.csv", index=False)
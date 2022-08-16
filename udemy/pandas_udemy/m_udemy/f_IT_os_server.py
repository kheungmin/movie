import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_IT_os_server.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("IT_os_server")

df.to_csv("p_IT_os_server.csv", index=False)
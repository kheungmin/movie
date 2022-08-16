import numpy as np
import pandas as pd
import numpy as np

df=pd.read_csv("p_devel_prg.csv")

df['category'] = np.NaN
df['category'] = df['category'].fillna("devel_prg_lang")

df.to_csv("p_devel_prg.csv", index=False)
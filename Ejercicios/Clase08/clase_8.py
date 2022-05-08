#%%
import numpy as np
import pandas as pd


#%%
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
# %%
s2.plot()
# %%

w = 5
s3 = s2.rolling(w).mean()
# %%
s3.plot()
# %%

df_series_23 = pd.DataFrame([s2, s3]).T
df_series_23.plot()
# %%

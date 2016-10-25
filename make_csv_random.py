import pandas as pd
import numpy as np

df = pd.read_csv('42.csv')
df['ts'] = pd.to_datetime(df.ts)
df = df.set_index('ts')

print df.head()

df = df.ix['2014']

print df.tail()

df.to_csv('42_random.csv')

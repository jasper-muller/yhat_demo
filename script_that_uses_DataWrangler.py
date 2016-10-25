from DataWrangler import DataWrangler

# WELCOME

dw = DataWrangler()
df = dw.read_data(42)

print('A glimpse at the initial DataFrame:')
print(df.head())

df_grouped_norm = dw.group_and_normalise(df)

print('\n .. and the result:')
print(df_grouped_norm.head())

# THE END

import pandas as pd

df1 = pd.read_csv('Book1.csv')
df2 = pd.read_csv('Book2.csv')

result = pd.merge(df1, df2, on='D_ID', how='inner')
#result = pd.merge(df1, df2, on='d_id', how='inner')
#print(df1)
#print(df2)
print(result)


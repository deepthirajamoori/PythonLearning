import pandas as pd

#with open('Sacramentorealestatetransactions.csv') as pan_file:
 #   pan_read = pd.read_csv(pan_file)
  #  print(pan_read)

df = pd.read_csv('Sacramentorealestatetransactions.csv')
#print(df)

#print(df.price.mean())
#print(df.describe())
#print(df[['street', 'price']][df.price==df['price'].min()])

df['flag'] = df['state'].apply(lambda x: '1' if x == 'CT' else '0')
print(df)

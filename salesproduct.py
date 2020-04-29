import pandas as pd
import timeit
import datetime
import numpy

df = pd.read_csv('SalesProducts.csv')

mycode = '''
def test_speed():
    z = datetime.datetime.now()
    df['flag'] = df['Year'].apply(lambda x: 1 if x >= 2013 else 0)
    x1 = df['Revenue'].sum() / df['Quantity'].sum()
    x2 = (df['Revenue'].sum() / df['Quantity'].mean())/(df.loc[df['flag'] == 1, 'Revenue'].sum()/df.loc[df['flag'] == 1,'Quantity'].mean())
    print(x2,x1)
    print(datetime.datetime.now()-z)
'''


print(timeit.timeit(stmt = mycode,number = 100000000))


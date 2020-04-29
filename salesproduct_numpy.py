import pandas as pd
import timeit
import datetime
import numpy as np

df = pd.read_csv('SalesProducts.csv')

mycode = '''
def test_speed():
    z = datetime.datetime.now()
    df['flag'] = np.where(df['Year'] >= 2013,1,0)
    x1 = df['Revenue'].values.sum() / df['Quantity'].values.sum()
    x2 = (df['Revenue'].values.sum() / df['Quantity'].values.mean())/(df.loc[df['flag'] == 1, 'Revenue'].sum()/df.loc[df['flag'] == 1,'Quantity'].mean())
    print(x2,x1)
    print(datetime.datetime.now()-z)
'''


print(timeit.timeit(stmt = mycode,number = 100000000))


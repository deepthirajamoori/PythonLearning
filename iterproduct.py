from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in product(a,b):
    print(i, end='')
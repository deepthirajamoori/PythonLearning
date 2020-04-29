x,k = map(int,input().split())
temp = 0
for i in range(0,k):
    temp += x**i

if temp == k:
    print(True)
else:
    print(False)

#print(temp)

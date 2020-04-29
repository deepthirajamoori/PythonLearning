N = int(input())
list_n = []
for i in range(n):
    if i<2:
        list_n += [+1]
    else:
        list_n += [list_n[-1]+list_n[-2]]
print(list_n)

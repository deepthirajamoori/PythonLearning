n = int(input())
el = []
for i in range(n):
    s = input()
    el.append(s)


empty_list = set(el)
#print(*empty_list,sep="\n")
print(len(empty_list))


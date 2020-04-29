n = int(input())
l1 = input().split()[:n]
s1 = set(l1)
m = int(input())
l2 = input().split()[:m]
s2 = set(l2)
print(len(s1.union(s2)))


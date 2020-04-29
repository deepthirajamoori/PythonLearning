Mnum = int(input())
M = list(int(num) for num in input().split())[:Mnum]
M = set(M)
Nnum = int(input())
N = list(int(num) for num in input().split())[:Nnum]
N = set(N)
O = (M.difference(N).union(N.difference(M)))
for i in sorted(list(O)):
    print(i)

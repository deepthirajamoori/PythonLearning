from itertools import combinations_with_replacement
a,n = input().split()
for i in range(1, int(n)+1):
    for j in combinations_with_replacement(sorted(a), i):
        print(''.join(j))
#for i in combinations(sorted(a),int(n)):
 #   print(*[''.join(i)],sep='\n')
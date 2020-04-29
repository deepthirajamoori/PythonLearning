from itertools import permutations
a,n = input().split()
for i in list(permutations(sorted(a),int(n))):
    print(*[''.join(i)],sep='\n')

N,X = map(int,input().split())
subject = []
zip_list = []
for i in range(0,X):
    sub = map(float,input().split()[:N])
    subject.append(list(sub))


zip_list = zip(*subject)
zip_list = list(zip_list)
final_sum = [sum(i)/len(i) for i in zip_list]
for i in final_sum:
    print(i)


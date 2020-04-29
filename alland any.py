n = int(input())
give_list = input().split()
print(all(int(i)>=0 for i in give_list) and any(i == i[::-1]for i in give_list))

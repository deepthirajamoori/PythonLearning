def fib(n):
    if n>=3:
        return fib(n-1)+fib(n-2)
    elif n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0

n = 5
temp_list = []
for i in range(n):
    temp_list.append(fib(i))
print(temp_list)




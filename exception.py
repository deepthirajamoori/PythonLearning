n = int(input())
for i in range(n):
    a,b = input().split()
    try:
        print(round(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

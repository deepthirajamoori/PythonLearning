def facto(n):
    if n>=1:
        return n * facto(n-1)
    elif n<0:
        print('please enter postive number')
    else:
        return 1


print(facto(10))
print(facto(5))

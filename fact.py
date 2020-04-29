a = 1
b = 0
def fact(n):
    global a
    global b
    global r
    if b == 0:
        r = n
    if n>a:
        x = n - a
        r = r * x
        a = a + 1
        b = b+1
        fact(n)
    return r

print(fact(10))
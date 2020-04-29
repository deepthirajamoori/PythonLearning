import re
n = int(input())
for i in range(n):
    s = input()
    try:
        reg = re.compile(s)
        print("True")
    except re.error:
        print("False")


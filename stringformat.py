def print_formatted(n):
# your code goes here
    for i in range(1, n+1):
        print (' ' + (str(i).rjust(len(str(i))).rjust((len(str(n))), ' ')) + (str(oct(i))[2:].rjust(len(str(bin(n))[2:])+1)) + ((str(hex(i))[2:].upper()).rjust(len(str(bin(n))[2:])+1)) + (str(bin(i))[2:].upper().rjust(len(str(bin(n))[2:])+1)))

print(print_formatted(17))
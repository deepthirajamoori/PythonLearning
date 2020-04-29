"""n = int(input())
numList = list(int(num) for num in input().strip().split(','))[:n]
numList = set(numList)
average = sum(numList)/len(numList)
print(average)"""

def average(array):
    n = int(input())
    array = list(int(num) for num in input().strip().split(','))[:n]
    array = set(array)
    average = sum(array)/len(array)
    return average

print(average)

#empty_list = list(map(int,input().split()))
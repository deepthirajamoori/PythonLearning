"""There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade 37.2 of  belongs to Tina. The second lowest grade 37.21 of  belongs to both Harry \
and Berry, so we order their names alphabetically and print each name on a new line."""
new_list = []
final_test = []
arr=[[input(),float(input())]  for i in range(int(input()))]
for i in arr:
        new_list.append(i[1])
        final_test = list(dict.fromkeys(new_list))
x = sorted(final_test)[1]
for i in arr:
        if x == i[1]:
                print(i[0])






"""if __name__ == '__main__':
    total = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        name_score = list((score, name))
        total.append(name_score)
    total.sort()
    min_mark = total[0][0]
    count = 0
    for i in range(len(total)):
        if min_mark == total[i][0]:
            count = count+1
    if count >= 1:
        for j in range(count):
            total.pop(0)
    nd_min_mark = total[0][0]
    for i in range(len(total)):
        if nd_min_mark == total[i][0]:
            print(total[i][1])"""







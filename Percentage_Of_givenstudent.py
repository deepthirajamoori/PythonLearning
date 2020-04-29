n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks.update({name:scores})
    print(student_marks)
query_name = input('outputStudent')
avg = sum(student_marks[query_name])/len(student_marks[query_name])
print("{:.2f}".format(avg))

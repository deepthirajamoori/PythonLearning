def count_substring(string, sub_string):
    string = input()
    sub_string = input()
    if string.find(sub_string)!= -1:
        return string.index(sub_string)

print(count_substring('asssdddffgg','sd'))

#list.index(element)

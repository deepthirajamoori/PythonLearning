def split_and_join(line):
    old = line[0].split()
    new = '-'.join(old)
    return new

line = ["this is a string"]
print(split_and_join(line))
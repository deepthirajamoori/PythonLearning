import csv

with open('Sacramentorealestatetransactions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for x in csv_reader:
        if line_count==0:
            print(f'Column names are {", ".join(x)}')
            print('/'.join(x))
            line_count += 1
        else:
            print(f'\t{x[0]}, {x[1]}, {x[2]}, {x[3]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

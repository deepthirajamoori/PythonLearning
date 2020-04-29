l1 = [2,3,4]
l2 = [3,6,8]
zip_list = list(zip(l1, l2))
print(zip_list)
a = lambda x: (print("The sum of (" + str(x[0]) +"," + str(x[1])+")" + "is " + str(x[0]+x[1])))
list(map(a, zip_list))

b = lambda y: (print("The sum of {} and {} is {}".format(y[0], y[1], y[0]+y[1])))
list(map(b, zip_list))



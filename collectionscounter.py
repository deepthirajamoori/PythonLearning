from collections import counter
num_list_of_shoe_sizes = int(input())
list_of_shoe_sizes = counter(list(map(int,input().split()))[:num_list_of_shoe_sizes])
customer_order_size = int(input())
shoe_size,price = map(int,input().split())
print(num_list_of_shoe_sizes)
print(list_of_shoe_sizes)
print(customer_order_size)
print(shoe_size,price,sep=" ")
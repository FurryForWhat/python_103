# 12,15,18   #100,1212,10
user = input('Enter three number by comma').split(',')  # ['100','1212','10']

first_data = int(user[0])   # first_data = 100
second_data = int(user[1])   # second_data = 1212
third_data = int(user[2])    #third_data = 10


if first_data > second_data:
    print(first_data,'is bigger than',second_data)
elif first_data == second_data:
    print(first_data,'is equal to',second_data)
else:
    print(first_data,'is smaller than',second_data)

if first_data > third_data:
    print(first_data,'is bigger than',third_data)
elif first_data == third_data:
    print(first_data,'is equal to',third_data)
else:
    print(first_data,'is smaller than',third_data)
my_data = input('Enter number').split(',')  #1,2,3,4
a = my_data[0] # a = '1'
b= my_data[1] # b = "2"  
c= my_data[2] # c= '3'
d = my_data[3] # d = '4'

a = int(a)  # a = 1
b = int(b)  # b = 2
c = int(c)  # c = 3
d = int(d)  # d = 4

even_num = 0
odd_num = 0

if a % 2 == 0: 
    even_num = even_num + 1
else:
    odd_num = odd_num + 1

if b % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1

if c % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1

if d % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1

print('Even number = ',even_num) # 2
print('Odd number =',odd_num) # 2
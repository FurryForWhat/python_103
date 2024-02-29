a = 4
b= 2
c = 3

if a > b:  #nested if
    print('a is bigger than b')
    if a > c:
        print('a is bigger than c')
    else:
        print('a is less than c')
else:
    print('a is smaller than b')
    if a > c:
        print('a is bigger than c')
    else:
        print('a is less than c')

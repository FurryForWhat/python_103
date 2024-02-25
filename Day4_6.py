a,c,d,e,f,g,i = True,True,True,True,True,True,True
b,h,j = False,False,False

first = a or b
second = c and d
third = e or f
fourth = g and h
fifth = i or j

one = first and second
two = third or fourth
three = not fifth

apple = one or two

final = apple and three
print(final)
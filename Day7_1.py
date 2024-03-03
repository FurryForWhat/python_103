user = input('Input Alphabet')#k
consonant = 0
vowel = 0

a = 'a'
e= 'e'
i = 'i'
o = 'o'
u = 'u'

if user == a:   #'k' == 'a'
    vowel += 1
elif user == e:
    vowel = vowel + 1
elif user == i:
    vowel += 1
elif user == o:
    vowel += 1
elif user == u:
    vowel += 1
else:
    consonant += 1

if consonant != 0:
    print(user,'is a consonant') #k is a constant
else:
    print(user,'is not a consonant')

if vowel != 0:
    print(user,'is a vowel')
else:
    print(user,'is not a vowel')
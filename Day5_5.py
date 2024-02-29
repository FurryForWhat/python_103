Name = input('Name :') #full column (:), semi column (;),single quote (')
Age = input('Age :')
Email = input('Email :')
password = input("Password:" )
             
name_search_cap = 'Aung'
name_search_small = 'aung'
if name_search_cap in Name:
    print('Found cap')
else:
    print('Not Found')

if name_search_small in Name:
    print('Found small')
else:
    print('not found')
    
age_search = 23
if age_search > 23:
    print("Allowed")
else:
    print('Not Allowed')

print('User Name: '+ Name + ' Age '+Age+' Email '+Email+' Password '+password)
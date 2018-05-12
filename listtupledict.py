#name = input("What is your name? ")
#age = int(input("How old are you? "))
#print('Your name is: %s and you are %d years old' %(name, age))


## [] - list
## () - tuple (list but immutable)
## {} - dictionary aka hash table

#list1=['Mher','Gago','Babo']
#print(list1)
#list1.insert(3, 'Nona')
#print(list1)

#tuple1=('Mher','Gago','Babo')
#print(tuple1)

dict1={'Mher':30,'Tami':26,'Gago':40}
print(dict1)

## Change Mher's age
dict1['Mher']=40
print(dict1)

## Add another person
dict1['Babo']=32
dict1['Karo']=50
print(dict1)

del dict1['Babo']
print(dict1)


## Looping through list

listnames=['Mher','Gago','Babo']
given_name=input("Please enter a name: ")

if given_name in listnames:
    print('We found this name')
else:print("There is no such name")

## Looping through dictionary

userdetails={'mher':'1111','jon':'1234','bob':'password'}

for password in userdetails.values():
    #print('\nUsername: '+username)
    print('Password: '+password)


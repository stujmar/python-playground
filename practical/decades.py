age = float(input("How old are you?\n"))
print (f'You are {age}')
print (f'You are {int(age//10)} decades old ...')
print (f'and an additional {int(age%10)} years :(\n')
if age > 50:
    print ("Wow you are old!")
else:
    print ("Wow you are young!")
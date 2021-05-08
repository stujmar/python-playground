length = 10
width = 20
area = length * width
print (area)


amount = float(input("What is your amount? "))
tax = float(input("What is your tax percentage? "))
total = amount + (amount * tax/100)
print (f'the amount plus tax is {total}')
# print ('the amount plus tax is ' + str(total))
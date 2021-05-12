expenses = [10.50, 8, 5, 15, 20, 5, 3]
my_sum = 0

for x in expenses:
    # sum = sum + x
    my_sum += x

total = sum(expenses)
print(total)
print("You spent $", my_sum, " on lunch.", sep='') # no seperation between strings.
print("Are theses the same? ", my_sum == total)

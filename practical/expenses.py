expenses = [10.50, 8, 5, 15, 20, 5, 3]
my_sum = 0

for x in expenses:
    # sum = sum + x
    my_sum += x

total = sum(expenses)
print(total)
print("You spent $", my_sum, " on lunch.", sep='') # no seperation between strings.
print("Are theses the same? ", my_sum == total)

your_expenses = []
num_expenses = int(input("How many expenses do you have? "))
for add in range(num_expenses):
    your_expenses.append(float((input("enter an expense:\n"))))

print(your_expenses)
print(sum(your_expenses))
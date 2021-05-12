# Let's get the details of the loan from the user
money_owed = float(input("How much do you owe in dollars? \n"))
apr = float(input("What is the annual interest rate? \n"))
payment = float(input("What is your monthly payment? \n"))
months = int(input("How many months do you want to see results for? \n"))

# Divide apr by 100 to make it a percent and 12 to make it monthly
monthly_rate = apr/100/12

for month in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    # Make a payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("Paid:", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)

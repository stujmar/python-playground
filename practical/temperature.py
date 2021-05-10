temp = input("what is the temperature?\n")
is_raining = True

if int(temp) > 90:
    print ("It sure is hot out.")
elif int(temp) < 32 and is_raining:
    print("Brrr. Watch out for freezing rain.")
elif int(temp) < 32 and not is_raining:
    print("Brrr.")
else:
    print("Have fun outside.")


temp = input("what is the temperature?\n")
forcast = "sun"

if int(temp) > 90:
    print ("It sure is hot out.")
elif int(temp) < 32 and forcast == "rain":
    print("Brrr. Watch out for freezing rain.")
elif int(temp) < 32 and not forcast == "rain":
    print("Brrr.")
else:
    print("Have fun outside.")


num_list = [1,2,3,4]
str_list = ["one", "two", "three", "four", "five"]
mix_list = ["five", 6, "seven", True]

print (mix_list)

mix_list.remove("five")

print (mix_list)

del mix_list[0] 

print (mix_list)

item = 4
if item in num_list:
    print ("4 is in num_list")
else:
    print (f"{item} is not in num_list")

answer = item in num_list
print (answer)

for number in str_list:
    print(number)
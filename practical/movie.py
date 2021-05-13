current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('Which movies would you like to see?\n')

show_time = current_movies[movie]

if show_time == None:
    print("There are no times for that movie.")
else:
    print(f"{movie} is playing at {show_time}")
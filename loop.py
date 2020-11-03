teams = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
}

c = 10
while c != 0:
    print("Go Team " + teams[c] + "!")
    c -= 1

def convert(input):
    number = ''
    for item in input:
        number += teams[item]
    x = int(number)
    return x
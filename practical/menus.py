menus = {
    'breakfast': ['eggs', 'bacon', 'juice'],
    'lunch': ['sandwich', 'orange', 'carrots'],
    'dinner': ['burger', 'pasta', 'wine']
}

for name, menu in menus.items():
    print(name, ':', menu)

for key, value in menus.items():
    print(key, ':', value)

person = {
    'name': "Stu",
    'city': 'Chicago',
    'age': 36
}

print(person.get('name'), 'is', person.get('age'), 'years old.')
contacts = {
    'number': 4,
    'students': [
        {'name': 'Sarah', 'email': 'sarah@example.com'},
        {'name': 'Stu', 'email': 'stu@example.com'},
        {'name': 'Ally', 'email': 'ally@example.com'},
        {'name': 'ShopCat', 'email': 'cat@example.com'},
    ]
}

emails = []

for student in contacts['students']:
    emails.append(student['email'])

print(emails)

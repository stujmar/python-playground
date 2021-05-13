import requests

# api.open-nofity.org/astros.json
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
# print(json)

print('The people currently in space are:')
for person in json['people']:
    print(person['name'], "in the", person['craft'])
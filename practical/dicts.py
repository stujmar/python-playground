# One way to add values to a dict
acronyms = {
    'LOL': "Laughing out loud",
    'IDK': "I don't know",
    'TBH': "to be honest"
}

print(acronyms['LOL'])

# Assign a new value
acronyms['ILY'] = 'I love you'

print(acronyms)

# del acronyms['LOL']

# print(acronyms)
# print(acronyms['OWL'])

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms['IDK'] + ' what happened ' + acronyms['TBH']

print(sentence)
print(translation)
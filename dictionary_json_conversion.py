import json

person = {'name': 'Bharat', 'age': 32, 'city': 'Bangalore', 'previousCompanies': ['cognizant', 'zycus', 'cerner'],
          'currentCompany': 'Thomson Reuters', 'isMarried': True}

# Serialization
personJson = json.dumps(person, indent=4, sort_keys=True)

print(personJson)

with open('json/person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Deserialization
person_deserialized = json.loads(personJson)
print(person_deserialized)

# using file

with open('json/person.json', 'r') as file:
    person_deserialized_from_file = json.load(file)
    print(person_deserialized_from_file)

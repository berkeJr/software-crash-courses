# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse json to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])
print(user['last_name'])
print(user['age'])


# Take a dictionary and turn it to JSON format.
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)
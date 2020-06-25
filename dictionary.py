# key value maps, or  an object in js

user = {'id': 1, 'name': 'John wick', 'email': 'john@gmail.com'}

print(user['name'])

# Length of the dict
print(len(user)) # 3

# Add new key-value pair
user['age'] = 35

print(user.keys()) #['email', 'age', 'id', 'name']
print(user.values()) #['john@gmail.com', 35, 1, 'John wick']

# To delete a key
del user['age']

# Example of nested dict.
user = {
  'id': 1,
  'name': 'John wick',
  'cars': ['audi', 'bmw', 'tesla'],
  'projects': [
    {
      'id': 10,
      'name': 'Project 1'
    },
    {
      'id': 11,
      'name': 'Project 2'
    }
  ]
}


print(user["projects"][0])
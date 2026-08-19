# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Cassie',
       'color': 'Brown',
       'breed': 'Shih Tzu',
       'legs': '4',
       'age': '15'
    }
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Tine',
           'last_name': 'De Castro',
           'gender': 'Female',
           'age': '18',
           'marital status': 'Single',
           'skills': ['Java', 'JavaScript', 'CSS', 'Node.JS'],
           'country': 'Philippines',
           'city': 'Pasay',
           'address': {
               'street': 'Rene',
               'zipcode': '15002'
            }
    }

print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('Python')
print(student)

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('country')

# Delete one of the dictionaries
del dog


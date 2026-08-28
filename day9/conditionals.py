# DAY 9 EXERCISES

# EXERCISE 1
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are old enough to drive.')
# else:
#     print('You need', 18-age, 'more years to learn to drive.')
   
# my_age = 18
# your_age = int(input('Enter your age: '))
# diff = your_age - my_age
# my_diff = my_age - your_age

# if your_age > my_age:
#     if diff == 1:
#         print('You are', diff,'year older than me.')
#     else:
#         print('You are', diff,'years older than me.')
# elif your_age == my_age:
#     print('You and I have the same age.')
# else:
#     if my_diff == 1:
#         print('I am', my_diff, 'year older than you.')
#     else:
#         print('I am', my_diff, 'years older than you.')

# number_one = int(input('Enter number one: '))
# number_two = int(input('Enter number two: '))

# if number_one > number_two:
#     print(number_one, 'is greater than', number_two)
# elif number_two > number_one:
#     print(number_one, 'is less than', number_two)
# else:
#     print('The two numbers are equal.')

# EXERCISE 2
# student_grade = int(input('Enter your score: '))

# if student_grade >= 90 and student_grade <= 100:
#     print('Your grade is A.')
# elif student_grade >= 80 and student_grade <= 89:
#     print('Your grade is B.')
# elif student_grade >= 70 and student_grade <= 79:
#     print('Your grade is C.')
# elif student_grade >= 60 and student_grade <= 69:
#     print('Your grade is D.')   
# elif student_grade >= 0 and student_grade <= 59:
#     print('Your grade is F.')
# else:
#     print('Your score is invalid.')
    
# month = input('Enter your birth month: ')

# if month.lower() == 'september' or month.lower() == 'october' or month.lower() == 'november':
#     print('Your season is autumn!')
# elif month.lower() == 'december' or month.lower() == 'january' or month.lower() =='february':
#     print('Your season is winter!')
# elif month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may':
#     print('Your season is spring!')
# elif month.lower() == 'june' or month.lower() == 'july' or month.lower() == 'august':
#     print('Your season is summer!')
# else:
#     print('The birth month is invalid.')
    
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit_input = input('Enter a fruit: ')

# if fruit_input in fruits:
#     print('That fruit already exists in the list.')
# else: 
#     fruits.append(fruit_input)
#     print('The fruit is added to the list, the modified list is:', fruits )

# Exercise 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# if 'skills' in person:
#     print('Skills exist for this person.')
#     print(person['skills'][2])
# else:
#     print('Bleh')
    
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person.get('skills', []):
        print('Python found!')
else:
    print('Wew')

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer.')

elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer.')
    
elif set(person.get('skills', [])) == {'JavaScript', 'React'}: # STRICTLY JS AND REACT ONLY
    print('He is a front end developer.')

else:
    print('Unknown title')
    
# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

if person.get('is_married') and 'Finland' in person['country']:
    print(person.get('first_name'), person.get('last_name'), 'lives in', person.get('country') + '.', 'He is married.')
    
else:
    print('Asbaneh is not married and does not live in Finland.')
    
    

 
# Day 2: 30 Days of python programming !!!

# EXERCISE LVL 1 YUP
first_name = 'Kristine'
last_name = 'Borres'
full_name = 'Kristine Borres'
country = 'Philippines'
city = 'Pasay'
age = 18
year = '2007'
is_married = False
is_true = True
is_light_on = True
hobby, music, movie = 'Gaming', 'August', 'The Odyssey' # declaring multiple variables in one line

# EXERCISE LVL 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(hobby))
print(type(music))
print(type(movie))

print(len(first_name))
print('Length of First Name:', len(first_name), '; Length of Last Name:', len(last_name)) # comparing the character length of the first name and last name

num_one = 5
num_two = 4

# add
total = num_one + num_two
print(total)

# minus
diff = num_two - num_one
print(diff)

# multiply
product = num_two * num_one
print(product)

# division
quotient = num_two / num_one
print(quotient)

# modulus
remainder = num_two % num_one
print(remainder)

# to the power of
exponent = num_one ** num_two
print(exponent)

# floor division
floor_division = num_two // num_two
print(floor_division)

radius = 30

# area of circle
area_of_circle =  3.14 * (radius ** 2)
print(area_of_circle)

# circumference of circle
circum_of_circle = 2 * (3.14 * radius)
print(circum_of_circle)

rad = int(input('Radius: '))
area_of_input = 3.14 * (rad ** 2)
print('Area:', area_of_input)

user_fname = input('Input your first name: ')
user_lname = input('Input your last name: ')
user_country = input('Input your country: ')
user_age = input('Input your age: ')

print('Welcome', user_fname, user_lname, 'from', user_country, ' with the age of', user_age)

    
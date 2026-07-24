# Day 3: 30 Days of python programming YASSS!!

# EXERCISE #1
age = 18
height = 160.02
complex = 14j

# finding the area of a triangle based on user's input on base and height
base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is', area)

# finding the perimeter of a triangle based on user's input on the 3 sides
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perimeter = a + b + c
print('The perimeter of the triangle is', perimeter)

# finding the area and perimeter of a rectangle
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
print('The area of the rectangle is', area)
perimeter2 = 2 * (length + width)
print('The perimeter of the triangle is', perimeter2)

# finding the radius of a circle
radius = float(input('Enter radius: '))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print('The area of the circle is', area)
print('The circumference of the circle is', circumference)

# getting the slope, x-intercept and y-intercept
xint = 1 # (1,0)
print('The x-intercept of y = 2x - 2 is', xint)
yint = -2 # (0,-2)
print('The y-intercept of y = 2x - 2 is', yint)
slope = (-2-0) / (0-1)
print('The slope of y = 2x - 2 is', slope)

# finding the slope and euclidean distance between (2,2) and (6,10)
slope2 = (10-2) / (6-2)
eucli = (2-2)**2 + (10-6)**2
print('The slope of the pair (2,2) and (6,10) is', slope2)
print('The euclidean distance between (2,2) and (6,10) is', eucli)
print('The slope of y = 2x - 2 and the pair (2,2) and (6,10) are the same')

x = -3
y = x**2 + (6*x) + 9
print('The value of y is', y)
# The value of x should be -3 in order for y to be 0.

# comparing the length of python and dragon and creating a false statement
print('The character length of python is', len('python'))
print('The character length of dragon is', len('dragon'))
print('The length of python and dragon are not equal:', len('python') != len('dragon'))

# using comparison
print('Is there a "jargon" in the sentence "I hope this course is not full on jargons"?', 'jargon' in 'I hope this course is not full on jargons')
print('Is there "on" in "jargon" and "python"?', 'on' in ('dragon' and 'python)'))

# finding the length of the text python and converting the value to float and convert it to string
pythonlength = len('python')
print(pythonlength)
floatpython = print(float(pythonlength))
stringpython = print(str(pythonlength))
print(type(stringpython))

# Checks if the user input is an even number or not
usereven = int(input('Input an even number: '))
sureven = usereven % 2 == 0
if sureven: 
    print('It is an even number!')
else:
    print('Your input is not an even number')
    
# floor division
convint = int(2.7)
print(convint)
floordiv = 7 // 3
print(floordiv)
ifequal = convint == floordiv
print(ifequal)

# check if '10' and 10 are equal or not
print(type('10'))
print(type(10))
print(type('10') == type(10))

# check if int('9.8') is equal to 10
# integ = int('9.8')
# print(integ == 10)
# # shows an error which means that they are not equal

# finding the weekly earning based on user input
hours = int(input('Enter hours: '))
rph = int(input('Enter rate per hour: '))
earning = hours * rph
print('Your weekly earning is', earning)

# calculating the number of seconds a person can live assuming a person can live a hundred years
yearslived = int(input('Enter number of years you have lived: '))
yeartosec = 31556952
secs = yearslived * yeartosec
print('You have lived for', secs, 'seconds')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')

    
    



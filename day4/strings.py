# DAY 4 STRING PRACTICE AND ACTIVITIES

# formatting string using the old and new way
a = 5
b = 6
formatted_string = ('{} + {} = {}' .format(a,b, a+b))
print(formatted_string)
formatted_float = ('{} - {} = {:.2f}') .format(a, b, a/b)
print(formatted_float)

# interpolation
c = 10
d = 23
print(f'{c} + {d} = {c+d}')

# sequences of characters 
subject = 'Mathematics'
a,b,c,d,e,f,g,h,i,j,k = subject
print(a)
print(b)
print(c)
print(d)

# gets last index
language = 'Python'
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# skipping characters
language = 'Python'
pto = language[0:6:2]  # start at index 0, stop before index 6, step by 2.
print(pto) # Pto

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1 # THIS INCLUDES THE SPACE BY THE WAY
print(challenge.count('th')) # 2`

# ACTIVIIES

# concatenating strings
thirty = ['Thirty', 'Days', 'Of', 'Python']
aresult = ' '.join(thirty)
print(aresult)

# other ways
first = 'Thirty' 
second = 'Days'
third = 'Of'
fourth = 'Python'
final = first + ' ' + second  + ' ' + third  + ' ' + fourth
print(final)

coding = ['Coding', 'For', 'All']
bresult = ' '.join(coding)
print(bresult)


company = 'Coding For All'
print(company)
print(len(company)) # finds the character length
print(company.upper()) # converts all to uppercase
print(company.lower()) # the opposite of upper
print(company.capitalize()) # capitalize every 1st char of the string
print(company.title()) # same with capitalize
print(company.swapcase()) # swap the casing
print(company[7:]) # start from the "For" and slice the first word
print(company.find('Coding')) # finds the index only
print('Coding' in company) # using the in (returns true or false)
print(company.replace('Coding For All', 'Python'))
print(company.split()) 
sites = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
allsites = ', '.join(sites)
print(allsites)
print(company[0]) # prints the character at index 0
print(company.rfind('l')) # returns last index
print(company[10]) # returns the space

pfe = 'Python For Everyone' # acronym 
cfa = 'Coding For All' 
cfp = 'Coding For All People'

print(cfa.find('C')) # find first occurence of C
print(cfa.find('F')) # find first occurence of F
print(cfp.rfind('l')) # find last occurence of l 

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
print(sentence[0:31] + sentence[55:]) # removes or splits the 'because because because'
# another way
print(sentence.replace('because because because', ''))

print(cfa.startswith('Coding'))
print(cfa.endswith('coding'))
print('   Coding For All      '.strip()) # removes whitespaces
print('30DaysOfPython'.isidentifier()) # returns false
print('thirty_days_of_python'.isidentifier()) # returns TRUE

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
alllibraries = ' '.join(libraries)
print(alllibraries)

print('\nI \nam \nenjoying \nthis \nchallenge.')
print('Name \tAge \tCountry \tCity \nAsbaneh 250 \tFinland \tHelsinki')

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# END OF ACTIVITY IN DAY 4: STRING
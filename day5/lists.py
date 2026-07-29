empty_list = list()

filled_list = list('example') # breaks down the word into characters
print(filled_list)

empty_list = [] 
filled_list = ['example', 'waeyo', 'jinjja'] # lists down the list inside the square bracket
print(filled_list)

print(len(filled_list)) # 3

lst = ['Kristine', 250, True, {'country':'Philippines', 'city':'Pasay'}] # different data types are allowed
print(lst)
print(len(lst))

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries # the *scandic includes all from denmark to iceland, excludes estonia since it is included
# in the unpacking list
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
print(orange_and_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']'

fruits[0] = 'avocado' # specify the index first then add the replacement
does_exist = 'banana' in fruits

list = []
list.append('item')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple orange and mango

fruits.remove('banana') 
fruits.pop(0) 
fruits.pop() 
del fruits[0]
del fruits[1:3] 
fruits.clear()
fruits_copy = fruits.copy() 

# START OF ACTIVITIES

empty_list = []
print(empty_list) # prints an empty list

brands = ['msi', 'acer', 'asus', 'rog', 'lenovo']
print(len(brands)) # finds the length of the brands list

threebrands = brands[::2] # gets the every 2nd step of the list 
print(threebrands)

mixed_data_types = ['Kristine', 18, 162.56, 'Single', 'Batumbakal 3 Ft']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[::3]) # prints the first, middle, and end of the list

it_companies[1] = 'Globe' # replace the 1st index with globe element
print(it_companies)

it_companies.append('DXC Technology') # add new element to the list
print(it_companies)

it_companies.insert(4, 'Yondu') # replace 4th index to yondu
print(it_companies)

it_companies[0] = it_companies[0].upper() # switch to uppercase the index 0 element
print(it_companies)

allcomp = ' #'.join(it_companies) # join or add a "#" to every start of the element
print(allcomp)

does_exist = 'Yondu' in allcomp # checks if there is yondu in the list
print(does_exist)

print(sorted(it_companies)) # sorts ascending
sort = sorted(it_companies, reverse=True) # sorts descending
print(sort)

some_companies = it_companies[:3] # only gets the first three
print(some_companies)

some2_companies = it_companies[6:] # only gets the last three
print(some2_companies)

middle_company = it_companies[4] # only gets the middle element
print(middle_company)

del it_companies[0] # remove first element
print(it_companies)

del it_companies[3:5] # removes the middle elements
print(it_companies)

it_companies.remove('DXC Technology') # removes the last element
print(it_companies)

it_companies.clear() # remove all companies from the list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)


# START OF EXERCISE 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

minage = ages[0]
maxage = ages[9]
print('Min age:', minage, 'Max age:', maxage)

print(len(ages))
print('Median age:', ages[4:6])

average = sum(ages)
print('Average age:', average/10)

range = maxage - minage
print('The range of the ages are', range)

minav = abs(minage - average)
maxav = abs(maxage - average)
print('The min age - average is', minav)
print('The max age - average is', maxav)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

print(len(countries))
print(len(countries)/2) # the middle or the median of the list

firsthalf = countries[:98] # the first half of the countries
# up till 98
print(firsthalf)
print(len(firsthalf))
print(countries[97]) # the 97 index (96 + 1 since 0 is counted) which marks the end of the first half

secondhalf = countries[98:] # prints the countries starting from 100th index
print(secondhalf)
print((len(secondhalf)))
print(countries[98]) 

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic)


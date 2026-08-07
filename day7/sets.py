it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# EXERCISE LEVEL 1

print(len(it_companies)) # finds the length of it_companies

it_companies.add('Twitter') # add twitter to the set
print(it_companies)

it_companies.update(['Accenture', 'DXC Technology', 'Yondu', 'Cloud Console']) # adding multiple companies
print(it_companies)

it_companies.remove('Microsoft') # remove microsoft from the set
print(it_companies)

# difference of remove and discard
print('The difference between remove and discard is that in remove, the removed item from the list is returned and can be stored in a variable, while the discard completely wipes the item in a list')

# EXERCISE LEVEL 2

print(A.union(B)) # joining a and b
print(A.intersection(B))  
print(A.issubset(B)) # is A a subset of B
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B

# EXERCISE LEVEL 3

agest = set(age)
print(agest) # age set
print(age) # age list

print(len(agest))
print(len(age)) 
# the bigger length is the age list, this is because it counts even the repeats, while the set only counts the repeated items as one.

word = 'I am a teacher and I love to inspire and teach people'
print(len(word))
splitted_word = word.split()
print(splitted_word)

unique_set = set(splitted_word)
print(unique_set)
# START OF ACTIVITIES FOR DAY 6 IN 30 DAYS OF PYTHON 
# notes in notes.txt

empty_tuple = tuple() # an empty tuple without any elements

brothers = ('Lawrence', 'Ivan') # tuple with elements
sisters = ('Aimee', 'Calypso')
siblings = brothers + sisters # joining the two tuples
print(siblings)

print(len(siblings)) # finding how many siblings there are

lst = list(siblings) # converts it to a list first in order to modify it
print(lst)

# modifying the list
lst.append('Glenn')
lst.append('Evangeline')
print(lst)

sibling_one, sibling_two, sibling_three, sibling_four, *parents = lst
siblings = []
siblings.append(sibling_one)
siblings.append(sibling_two)
siblings.append(sibling_three)
siblings.append(sibling_four)
print('My siblings are:', siblings)
print('My parents are:', parents)

mysiblings = tuple(siblings) # change the list back to tuple
myparents = tuple(parents)
print(mysiblings)
print(myparents)

fruits = ('apple', 'mango', 'orange')
vegetables = ('lettuce', 'asparagus', 'onion')
animal_products = ('meat', 'egg', 'milk')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))

print(food_stuff_lt[4])
middle_item = food_stuff_lt[4]
print(middle_item)

first_three = food_stuff_lt[:3]
print(first_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)



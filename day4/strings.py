# day 4 string practice

a = 5
b = 6

formatted_string = ('{} + {} = {}' .format(a,b, a+b))
print(formatted_string)

formatted_float = ('{} - {} = {:.2f}') .format(a, b, a/b)
print(formatted_float)

#interpolation
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

language = 'Python'
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

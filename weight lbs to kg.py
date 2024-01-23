# input from user
weight_lbs = input('enter your weight(lbs): ')
weight_kg = int(weight_lbs) * 0.45
# see the type of variable
print(type(weight_kg))

# comment
course ='''
"Python's for Beginners " 
Hey bro, I'm practice coding ....

thank you
From Ashish
'''
print(course)

print(course[0:50])

# formatted string
first = 'Ashish'
last = 'kumar'
# string method
message = f'{first} {[last]} is a coder'

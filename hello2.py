name = 'Daniel'
age = 33

def print_user(name, age):
    print('Welcome,', name, '. You are currently', age, 'years old.')
    return

print_user(name, age)

def get_inputs():
    firstname = input('First name: ')
    lastname = input('Last name: ')
    age = input('Age: ')
    print(firstname, lastname, age)

get_inputs()

## if else statements

def driving_age(age):
    if(age < 18):
        print('You are not old enough to drive')
    elif(age >= 18):
        print('driving...')

driving_age(age)

## loops
# FOR loop

days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

for d in days:
    print(d)

## while loop

x = 3

while(x <= 10):
    print(x)
    x = x + 1


Thomas_Age = 6
Age_At_Kindergarden = 5 

if Thomas_Age < Age_At_Kindergarden:
    print('Thomas should be in pre-school')
elif Thomas_Age == Age_At_Kindergarden:
    print('Thomas should be in kindergarden')
else:
    print('Thomas should be in another class')

def print_daniel():
    text = 'Daniel is a Brazilian-Israeli Frontend Software Engineer'
    print(text)

print_daniel()

def driving_age(age, name):
    if age >= 18:
        print(name, 'you are old enough to drive')
    elif age < 18:
        print(name, 'you are NOT old enough to drive')

driving_age(33, 'Daniel')

#loops
# while loop:

x = 0
while(x < 10):
    print(x)
    x = x+1

# for loop:

for y in range(5,10):
    print('y =', y)

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for day in days:
    print(day)

for d in days:
    if(d == 'Thu'):break
    print('day is:', d)

for d in days:
    if(d == 'Thu'):continue
    print('day:', d)

def soma(num1, num2):
    print(num1 + num2)

soma(30, 50)

first = input('First: ')
second = input('Second: ')

sum = float(first) + float(second)
print('Sum equals ', sum)
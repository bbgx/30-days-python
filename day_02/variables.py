# Day 2: 30 Days of Python Programming

# Exercise: Level 1

# Define variables
first_name = "bbgx"
last_name = "bgmnn"
full_name = "bbgx bgmnn"
country = "Brazil"
city = "Detroit"
age = 32
year = 2023
is_married = False
is_true = True
is_light_on = True
name, legs, hands = "bbgx", 2, 2

# Exercise: Level 2

print('------- Exercises: Level 2 -------')

# Check data type of variables
print('Check the data type of all your variables using type() built-in function')
print('First name type: ', type(first_name))
print('Last name type: ', type(last_name))
print('Full name type: ', type(full_name))
print('Country type: ', type(country))
print('City type: ', type(city))
print('Age type: ', type(age))
print('Year type: ', type(year))
print('Is married type: ', type(is_married))
print('Is true type: ', type(is_true))
print('Is light on type: ', type(is_light_on))
print('Name type: ', type(name))
print('Legs: ', type(legs))
print('Hands: ', type(hands))

# Get the length of first_name
print('The first name length is: ', len(first_name))

# Compare the length of first_name and last_name
while True:
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')

    if last_name == "" or first_name == "":
        print('Sorry, you should input a first and/or last name.')
    else:
        break

def checkNames(first_name, last_name):
    """A function that compares the length of first_name and last_name"""
    first_name_length = len(first_name)
    last_name_length = len(last_name)

    if first_name_length > last_name_length:
        print('Your first name is longer than your last name.')
    elif last_name_length > first_name_length:
        print('Your last name is longer than your first name.')
    elif last_name_length == first_name_length:
        print('They\'re both the same size :)')

checkNames(first_name, last_name)

# Declare variables and perform arithmetic operations
print('Declare 5 as num_one and 4 as num_two ')
num_one = 5
num_two = 4
total = num_one + num_two
print('The sum of those numbers are: ', total)
diff = num_two - num_one
print('The subtraction of those numbers are: ', diff)
product = num_two * num_one
print('The product of those numbers are: ', product)
division = num_one / num_two
print('The division of those numbers are: ', division)
remainder = num_two % num_one
print('The modulus of those numbers are: ', remainder)
exp = num_one ** num_two
print('The exponential of those numbers are: ', exp)
floor_division = num_one // num_two
print('The floor division of those numbers are: ', floor_division)

# Calculate area and circumference of a circle
print('The radius of a circle is 30 meters.')
radius = 30
pi = 3.14159

circum_of_circle = 2 * pi * radius
print('The circunference of this circle is: ', circum_of_circle)

# Calculate area of a circle with user input
def calculateArea():
    """A function that calculates the area of a circle with user input"""
    radius = input('What is the radius of your circle?\n')
    area_of_circle = pi * (float(radius) ** 2)
    print('The area of the circle is: ', area_of_circle)
calculateArea()

def getUserInformation():
    """A function that prompts the user to enter their information"""
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    country = input('Where do you live?\n')
    age = input('How old are you?\n')
    print(f"""Check the user information:
    His first name is: {first_name}.
    His last name is: {last_name}.
    He is living in: {country}.
    His age is: {age}.
    Nice to meet you {first_name}!""")
    
getUserInformation()

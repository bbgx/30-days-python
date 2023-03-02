# 30 Days of Python Programming
## Day 2: Exercises
## Exercise Level 1
In this exercise, we define some variables with different data types:
```python
first_name = "bbgx"               # Declare a first name variable and assign a value to it
last_name = "bgmnn"               # Declare a last name variable and assign a value to it
full_name = "bbgx bgmnn"          # Declare a full name variable and assign a value to it
country = "Brazil"                # Declare a country variable and assign a value to it
city = "Detroit"                  # Declare a city variable and assign a value to it
age = 32                          # Declare an age variable and assign a value to it
year = 2023                       # Declare a year variable and assign a value to it
is_married = False                # Declare a variable is_married and assign a value to it
is_true = True                    # Declare a variable is_true and assign a value to it
is_light_on = True                # Declare a variable is_light_on and assign a value to it
name, legs, hands = "bbgx", 2, 2  # Declare multiple variable on one line
```
## Exercise Level 2
In this exercise, we check the data type of each variable using the type() function:
```python
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
```
Next, we get the length of the first_name variable using the len() function:
```python
print('The first name length is: ', len(first_name))
```
We then ask the user to enter their first and last names and compare their lengths using the checkNames() function:
```python
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
```
Next, we declare two variables and perform arithmetic operations with them:
```python
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
```
Then, we calculate the circumference of a circle with radius 30 meters and assign it to a variable:
```python
print('The radius of a circle is 30 meters.')
radius = 30
pi = 3.14159

circum_of_circle = 2 * pi * radius
print('The circumference of this circle is: ', circum_of_circle)
```
We also define a function called calculateArea() to calculate the area of a circle with user input:
```python
def calculateArea():
    """A function that calculates the area of a circle with user input"""
    radius = input('What is the radius of your circle?\n')
    area_of_circle = pi * (float(radius) ** 2)
    print('The area of the circle is: ', area_of_circle)
calculateArea()
```
Finally, we define a function called getUserInformation() to prompt the user to enter their first name, last name, country, and age, and then print out their information:
```python
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
```

The output of the program will prompt the user for input and display the results of the different calculations and functions performed.

## Conclusion
In this exercise, we learned about variable assignment and data types in Python. We also used different built-in functions to perform arithmetic operations and check the data type of variables. We also created functions to calculate the area and circumference of a circle and prompt the user for input to print out their personal information. This exercise provided a good introduction to some of the basic concepts of Python programming.

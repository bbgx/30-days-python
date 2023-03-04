# Declare your age as integer variable
age = 55
# Declare your height as a float variable
heigth = 1.85
# Declare a variable that store a complex number
complex_number = 3.14j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
heigth = float(input("Enter height: "))
triangle_area = 0.5 * base * heigth
print(f"The area of the triangle is {triangle_area}cm²")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}cm")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is {perimeter}cm and the area this {area}cm²")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
circumference  = 2 * 3.14159 * radius
print(f"The area of the circle is {area}cm and the circumference this {circumference}cm²")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
def equation(x):
    return 2*x - 2
slope1 = 2
x_intercept = 1
y_intercept = equation(0)
print(f"Slope: {slope1}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point1 = [2, 2]  # (x1, y1)
point2 = [6, 10] # (x2, y2)
slope2 = (point2[1] - point1[1]) / (point2[0] - point1[0])
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
print(distance)
print(slope2)
 
# Compare the slopes in tasks 8 and 9.
if slope1 > slope2:
    print('Your slope1 is longer than your slope2.')
elif slope2 > slope1:
    print('Your slope2 is longer than your slope1.')
elif slope2 == slope1:
    print('They\'re both the same size :)')

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
while True:
    x = float(input("Enter X: "))
    y = x**2 + 6*x + 9
    print(y)
    if y == 0:
        break
# The number is -3

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") != len("dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in ("python" and "dragon"))

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# There is no 'on' in both dragon and python
print("on" not in ("python" and "dragon"))

# Find the length of the text python and convert the value to float and convert it to string
text = float(len(input("Enter you text: ")))
print(f"float {type(text)}")
print(f"str {type(str(text))}")

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = float(input("Throw a number for me: "))
if (number % 2) == 0:
    print("This number is odd my guy")
else:
    print("This number is even my guy")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor = 7 // 3
print(floor == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(float("9.8")) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
work_hours = int(input("Enter hours: "))
work_rate = float(input("Enter rate per hour: "))
weekly_earn = work_hours * work_rate
print(f"Your weekly earning is {weekly_earn}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
year_to_sec = years * 31536000
print(f"You have lived for {year_to_sec} seconds.")

# Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
x x**0 x**1 x**2 x**3
"""
for x in range(1, 6):
    print(x, end=" ")
    for j in range(0, 4):
        print(x**j, end=" ")
    print()
# 30 Days of Python Programming
## Day 3: Exercises

- Declare your age as integer variable

```python
age = 55
```
- Declare your height as a float variable

```python
heigth = 1.85
```
 - Declare a variable that stores a complex number

```python
complex_number = 3.14j
``````
 - Calculate the area of a triangle

```python
base = float(input("Enter base: "))
heigth = float(input("Enter height: "))
triangle_area = 0.5 * base * heigth
print(f"The area of the triangle is {triangle_area}cm²")
``````
 - Calculate the perimeter of a triangle

```python
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}cm")
```
 - Calculate the area and perimeter of a rectangle

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is {perimeter}cm and the area this {area}cm²")
```
 - Calculate the area and circumference of a circle

```python
radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
circumference  = 2 * 3.14159 * radius
print(f"The area of the circle is {area}cm and the circumference this {circumference}cm²")
```
 - Calculate the slope, x-intercept, and y-intercept of y = 2x - 2

```python
def equation(x):
    return 2*x - 2
slope1 = 2
x_intercept = 1
y_intercept = equation(0)
print(f"Slope: {slope1}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")
```
- Calculate the slope and Euclidean distance between two points

```python
point1 = [2, 2]  # (x1, y1)
point2 = [6, 10] # (x2, y2)
slope2 = (point2[1] - point1[1]) / (point2[0] - point1[0])
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
print(distance)
print(slope2)
```
- Compare the slopes in tasks 8 and 9

```python
if slope1 > slope2:
    print('Your slope1 is longer than your slope2.')
elif slope2 > slope1:
    print('Your slope2 is longer than your slope1.')
elif slope2 == slope1:
    print('They\'re both the same size :)')
```
- Calculate the value of y (y = x^2 + 6x + 9) and find the value of x when y = 0

```python
while True:
    x = float(input("Enter X: "))
    y = x**2 + 6*x + 9
    print(y)
    if y == 0:
        break
# The number is -3
```
- Find the length of 'python' and 'dragon' and make a falsy comparison statement

```python
print(len("python") != len("dragon"))
```
- Use the and operator to check if 'on' is found in both 'python' and 'dragon'

```python
print("on" in ("python" and "dragon"))
```
- Use the in operator to check if 'jargon' is in the sentence 'I hope this course is not full of jargon'

```python
print("jargon" in "I hope this course is not full of jargon")
```
- Check that there is no 'on' in both 'dragon' and 'python'

```python
print("on" not in ("python" and "dragon"))
```
- Find the length of the text 'python', convert it to a float and then convert it to a string

```python
text = float(len(input("Enter your text: ")))
print(f"float {type(text)}")
print(f"str {type(str(text))}")
```
- Check if a number is even or odd using the modulo operator

```python
number = float(input("Enter a number: "))
if (number % 2) == 0:
    print("This number is even")
else:
    print("This number is odd")
```
- Check if the floor division of 7 by 3 is equal to the integer converted value of 2.7

```python
floor = 7 // 3
print(floor == int(2.7))
```
- Check if the type of '10' is equal to the type of 10

```python
print(type('10') == type(10))
```
- Check if int('9.8') is equal to 10

```python
print(int(float("9.8")) == 10)
```
- Write a script that prompts the user to enter hours worked and rate per hour, then calculates the pay of the person

```python
work_hours = int(input("Enter hours worked: "))
work_rate = float(input("Enter rate per hour: "))
weekly_earn = work_hours * work_rate
print(f"Your weekly earning is {weekly_earn}")
```
- Write a script that prompts the user to enter the number of years they have lived, then calculates the number of seconds a person can live (assuming a person can live up to 100 years)

```python
years = int(input("Enter number of years you have lived: "))
year_to_sec = years * 31536000
print(f"You have lived for {year_to_sec} seconds.")
```
- Write a Python script that displays a table

```python
for x in range(1, 6):
    print(x, end=" ")
    for j in range(0, 4):
        print(x**j, end=" ")
    print()
```
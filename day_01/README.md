# Exercises in Python
This repository contains a Python script with exercises to practice different concepts and data types in Python.

## Level Two
### Exercise 1
This exercise involves performing different arithmetic operations in Python.
```python
print('-------- LEVEL TWO -------')
print('------- exercise 1 -------')
print(3 + 4)  # addition(+)
print(3 - 4)  # subtraction(-)
print(3 * 4)  # multiplication(*)
print(3 % 4)  # modulus(%)
print(3 / 4)  # division(/)
print(3 ** 4) # exponential(**)
print(3 // 4) # Floor division operator(//)
```
### Exercise 2
This exercise involves printing different strings in Python.
```python
print('------- exercise 2 -------')
print("bbgx")
print("bgmnn")
print("Brazil")
print("I am enjoying 30 days of python")
```
### Exercise 3
This exercise involves identifying the data type of different variables in Python.
```python
print('------- exercise 3 -------')
print(type(10))                                  # int
print(type(9.8))                                 # float
print(type(3.14))                                # float
print(type(4 - 4j))                              # complex
print(type(['Asabeneh', 'Python', 'Finland']))   # list
print(type("bbgx"))                              # string
print(type("bgmnn"))                             # string
print(type("Brazil"))                            # string
```
## Level Three

This level involves practicing different data types in Python.
### Integer
```python
print('------ LEVEL THREE -------')
print('--------- integer --------')
n_int = 10
print(type(n_int))
```
### Float
```python
print('-------- complex ---------')
n_complex = 3.14j
print(type(n_complex))
```
### Complex
```python
print('-------- complex ---------')
n_complex = 3.14j
print(type(n_complex))
```
### Boolean
```python
print('--------- boolean --------')
boolean = True
print(type(boolean))
```
### List
```python
print('----------- list ---------')
list = ['bbgx', 'Brazil', 'Cleiton']
print(type(list))
```
### Tuple
```python
print('----------- tuple ---------')
tuple = ('bbgx', 'Brazil', 'Cleiton')
print(type(tuple))
```
### Set
```python
print('------------ set ----------')
set = set(('bbgx', 'Brazil', 'Cleiton'))
print(type(set))
```
### Dictionary
```python
print('------------ dictionary ----------')
dictionary = {'name': 'bbgx', 'country': 'Brazil', 'friend': 'Cleiton'}
print(type(dictionary))
```
### Euclidean Distance
This exercise involves calculating the Euclidean distance between two points in a two-dimensional space.
```python
print('- Find an Euclidian distance between (2, 3) and (10, 8) -')
# Define the coordinates of the two points
point1 = [2, 3]  # (x1, y1)
point2 = [10, 8] # (x2, y2)
# Calculate the Euclidean distance between the two points
# distance = √((x2 - x1)^2 + (y2 - y1)^2)
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
# The Euclidean distance formula calculates the square root of the sum of the squares of the differences between the x and y coordinates of the two points.
# Output the distance to the console
print(distance)
```
This code defines the coordinates of two points (2, 3) and `(10, 8)

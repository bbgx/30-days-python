print('-------- LEVEL TWO -------')
print('------- exercise 1 -------')
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

print('------- exercise 2 -------')
print("bbgx")
print("bgmnn")
print("Brazil")
print("I am enjoying 30 days of python")

print('------- exercise 3 -------')
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("bbgx"))
print(type("bgmnn"))
print(type("Brazil"))

print('------ LEVEL THREE -------')
print('--------- integer --------')
n_int = 10
print(type(n_int))
print('---------- float ---------')
n_float = 3.1415
print(type(n_float))
print('-------- complex ---------')
n_complex = 3.14j
print(type(n_complex))
print('--------- string ---------')
str = "bbgx"
print(type(str))
print('--------- boolean --------')
boolean = True
print(type(boolean))
print('----------- list ---------')
list = ['bbgx', 'Brazil', 'Cleiton']
print(type(list))
print('----------- tuple ---------')
tuple = ('bbgx', 'Brazil', 'Cleiton')
print(type(tuple))
print('------------ set ----------')
set = set(('bbgx', 'Brazil', 'Cleiton'))
print(type(set))
print('------------ dictionary ----------')
dictionary = {'name': 'bbgx', 'country': 'Brazil', 'friend': 'Cleiton'}
print(type(dictionary))
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

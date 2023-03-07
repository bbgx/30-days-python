# Day 4: 30 Days of Python Programming

# Exercises

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty ' + 'Days ' + 'Of ' + 'Python')
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding ' + 'For ' + 'All')
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[7:])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
# Change Python for Everyone to Python for All using the replace method or other methods.
print("Python for Everyone".replace("Everyone", "All"))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
# What is the character at index 0 in the string Coding For All.
print("Coding For All"[0])
# What is the last index of the string Coding For All.
print("Coding For All"[-1])
# What character is at index 10 in "Coding For All" string.
print("Coding For All"[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
f_letter = [letter[0] for letter in name.split()]
acronym = "".join(f_letter)
print(acronym)
# Use index to determine the position of the first occurrence of C in Coding For All.
print("Coding For All".index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print("Coding For All".index("F"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All".rfind("l"))
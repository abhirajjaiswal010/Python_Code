# data_types.py

# 1. Integer (int) → Whole numbers (positive or negative)
age = 20
print(age, type(age))   # Output: 20 <class 'int'>

# 2. Float (float) → Numbers with decimals
pi = 3.14
print(pi, type(pi))     # Output: 3.14 <class 'float'>

# 3. String (str) → Sequence of characters (text)
name = "Abhiraj"
print(name, type(name)) # Output: Abhiraj <class 'str'>

# 4. Boolean (bool) → True or False values
is_student = True
print(is_student, type(is_student))  # Output: True <class 'bool'>

# 5. List (list) → Ordered, changeable collection (can contain mixed data types)
fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))  # Output: ['apple', 'banana', 'cherry'] <class 'list'>

# 6. Tuple (tuple) → Ordered, unchangeable collection
coordinates = (10, 20)
print(coordinates, type(coordinates)) # Output: (10, 20) <class 'tuple'>

# 7. Set (set) → Unordered, unique elements only
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers, type(unique_numbers)) # Output: {1, 2, 3} <class 'set'>

# 8. Dictionary (dict) → Key-value pairs
student = {"name": "Abhiraj", "age": 20, "course": "CS"}
print(student, type(student))  # Output: {'name': 'Abhiraj', 'age': 20, 'course': 'CS'} <class 'dict'>

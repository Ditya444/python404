# 1. How Do You Declare Variables and
# What Are Naming Conventions to Name Variables?

name = 'John Doe'
age = 25

# Variable names should be in lowercase and separated by an underscore

variable_name = 'Python404'

# Use descriptive name for variable
user_name = "Tester"

# Single-line comment

# Multi-line
# comment


# 2. Print Function

print('Hello world!') # Hello world!

print('My favorite colors are', 'blue', 'green', 'red') 
# Output: My favorite colors are blue green red


# 3. Common data types in Python

name = 'John Doe' # Python knows this is a string
age = 25 # Python knows this is an integer(number)

# - Integer: A whole number without decimals, for example, 10 or -5.
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

# - Float: A number with a decimal point, like 4.41 or -0.4.
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5

# - String: A sequence of characters enclosed in single or 
# double quotation marks like 'Hello world!'
my_string_var = 'hello'
print('String:', my_string_var) # String: hello

#  - Boolean: A true or false type, written as True or False.
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

# - Set: An unordered collection of unique elements, like {0.5, 4, 'apple'}
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {8.5, 'hello', 7} (order may vary)

# - Dictionary: A collection of key-value pairs enclosed in curly braces, 
# like {'name': 'John Doe', 'age': 28}
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

# - Tuple: An immutable ordered collection, enclosed in parentheses, like ('apple', 4.5, 7)
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)

# - Range: A sequence of numbers, often used in loops, for example, range(5)
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)

# - List: An ordered collection of elements that supports different data types.
my_list_var = [22, 'Hello world', 3.14, True]
print('List:', my_list_var) # List: [22, 'Hello world', 3.14, True]

#  - None: A special value that represents the absence of a value.
my_none_var = None
print('None:', my_none_var) # None: None


#  4. type() and isinstance() Functions


# View the type of a variable, type()
developer = 'Devin'

print(type(developer)) # <class 'str'>
# The output of <class 'str'> means that developer is a string type.

# type() error message:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: type() takes 1 or 3 arguments

# All data types with type() functions prints
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

# isintance() functions
# To verify that a particular variable is a specific type before performing operations on it
account_balance = '12'

account_balance / 2

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# To see if account_balance is an integer, 
# you can check using the isinstance() function like this:
account_balance = '12'

isinstance(account_balance, int) # False

account_balance = 12
isinstance(account_balance, (int, float)) # True
# In this example, account_balance is an integer so isinstance() returns True. 
# If account_balance were 12.0,  isinstance() would still return True 
# because you are checking for integers or floats.

# 1. What Are Strings and What is String Immutability?

# A string is a sequence of characters surrounded by either single 
# or double quotation marks
my_str_1 = 'Hello'
my_str_2 = 'World'

# multi-line string
my_str_3 = '''Multiline 
string'''
my_str_4 = '''Another
multiline
string'''

# if strings containts quotation marks
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Escape quotation mark in string with a backslash (\)
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# in operator, which returns a boolean that specifies whether the 
# character or characters exist in the string or not.
my_str = "Hello world"

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False


# Set the length of a string and work with the individual characters 
# in a string, a process called indexing
# built-in len() function to get the length of a string
my_str = "Hello world"
print(len(my_str)) #11

# Index is the position of the string.
# Index is zero-based (start with 0 and so on)
# use ([]) to access character by its index
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w

# Negative indexing, the last character of any string with -1 and so on
print(my_str[-1])  # d
print(my_str[-2]) # l

# Mutable value can be changed
# Immutable calue cannot be changed

# Reassigment is where a variable pointed at a new value
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# direct modification is not allowed
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment



# 2. What Are String Concatenation and String Interpolation

# Concatenating Strings
# Combine multiple strings with (+) operator
# The process is called string concatenation
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# Repeating Strings
# Repeat a string by multiplying it with an integer using *
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) #hahaha

# Concatenating Strings with Numbers
# Concatenate a string with a number, you'll get a TypeError
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# Python does not automatically convert other data types like integers
# into strings when you concatenate them. 
# Python requires all elements to be strings before it 
# can concatenate them. 

# Fix it by convert the number into string with str() function
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

# Augmented assignment operation for concatenation
# Represented by a plus and equal sign (+=)
# Performs both concatenation and assignment in one step
name = 'John Doe'
age = 26

name_and_age = name # Start with the name
name_and_age += str(age) # Append the age as string

print(name_and_age) # John Doe26


# String Interpolation
# String interpolation is a process of inserting variables and
# expressions into a string.
# String called f-strings(formatted string literals), allows to
# handle interpolation with a compact and readable syntax.

# F-strings start with f(lowercase or uppercase) before the quotes,
# allowing to embed variables or expressions inside replacement
# fields indicated by curcly braces({}).
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
# In the example above, the value of the age, num1, and num2 variables
# is converted under the hood into a string during the interpolation process.



# 3. What is String Slicing and How Does It Work?
# Identify string by index and accesed it using []
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

# String slicing extract a portion of a string or work with only specific part
# string[start:stop]
my_str = "Hello world"
print(my_str[1:4]) # ell

# Stop index is non-inclusive, meaning [1:4] just extracted the characters from index 1,
# and up to, not including char at index 4

# If you omit the start and stop indices, python will default it to 0 or the end of the string
# omit start
my_str = "Hello world"
print(my_str[:7]) # Hello w

# omit stop
print(my_str[8:0]) # rld

# Slicing a string does not modify original string
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

# Step parameter used to specify the increment between each index in the slice
# the syntax: string[start:stop:step]
# Example below shows slicing starts at idnex 0, stops before 11, and extract every
# second character:
my_str = "Hello world"
print(my_str[0:11:2]) # Hlowrd

# A trick to use step parameter is to reverse a string by setting step to -1, and leaving
# start and stop blank:
step_trick = "Hello world"
print(step_trick[::-1])



# 4. Common String Methods
# Method is a function that you cal on a value
# Method can be called by writing the string or its variable name followed by a dot and 
# the method call

# upper(): Returns a new string with all chars converted to uppercase
upperMethod_str = "hello world"

uppercase_upperMethod_str = my_str.upper()
print(uppercase_upperMethod_str) # HELLO WORLD

# lower(): Returns a new string with all chars converted to lowercase
lowerMethod_str = "HELLO WOLRD"

lowercase_lowerMethod_str = lowerMethod_str.lower()
print(lowercase_lowerMethod_str) #hello world

# strip(): Returns a new string with the specified leading and trailing characters
# removed. If no argument is passed it removes leading and trailing whitespace
stripMethod_str = ' hello world '

trimmed_stripMethod_str = stripMethod_str.strip()
print(trimmed_stripMethod_str) # "hello world"

# replace(old, new): Returns a new string with all occurrences of old replaced by new
replaceMethod_str = 'hello world'

replaced_replaceMethod_str = replaceMethod_str.replace("hello", "hi")
print(replaced_replaceMethod_str) #hi world

# split(separator): Splits a string on a specified separator into a list of strings.
# A list groups values between square brackets.
# If no separator is specified, split() splits on whitespace
splitMethod_str = 'hello world'

split_words = splitMethod_str.split()
print(split_words) #['hello', 'world']

# join(): Joins the strings in a collection into a single string with a separator
join_list = ['hello', 'world']

joined_join_list = ' '.join(join_list)
print(joined_join_list) # hello world

# startswith(prefix): Returns a boolean indicating if a string starts with the
# specified prefix
startWith_str = 'hello world'

starts_with_hello = startWith_str.startswith('hello')
print(starts_with_hello) # True

# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix
endsWith_str = 'hello world'

ends_with_world = endsWith_str.endswith('world')
print(ends_with_world) # True

# find(substring): Returns the index of the first occurrence of substring
# -1 if it does not find one
find_str = 'hello world'

world_index = find_str.find('world')
print(world_index) # 6

# count(substring): Returns the number of time a substring appears in a string
count_str = 'hello world'
o_count = count_str.count('o')
print(o_count) # 2

# capitalize(): Returns a new string with the first character capitalized and 
# the other characters lowercased.
cap_str = 'hello world'

capitalized_cap_str = cap_str.capitalize()
print(capitalized_cap_str) # Hello world

# isupper(): Returns True if all letters in the string are uppercase and False if not
isUpper_str = 'hello world'

is_all_upper = isUpper_str.isupper()
print(is_all_upper) # False

# islower(): Returns True if al letters in the string are lowercase and False if not
isLower_str = 'hello world'

is_all_lower = isLower_str.islower()
print(is_all_lower) # True

# title(): Returns a new string with the frist letter of each word capitalized
title_str = 'hello world'

title_case_my_str = title_str.title()
print(title_case_my_str) # Hello World






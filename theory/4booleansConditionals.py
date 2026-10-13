# Booleans and Conditionals
# Conditional statements, or conditionals, control the flow of the
# program based on whether certain conditions are true or false

# Comparison Operators
# Table of comparison operators in Python:
comparison_table = """
| Operator | Name                  | Example | 
|----------|-----------------------|---------|
| ==       | Equal                 | x == y  |
| !=       | Not equal             | x != y  |
| >        | Greater than          | x > y   |
| <        | Less than             | x < y   |
| >=       | Greater than or equal | x >= y  |
| <=       | Less than or equal    | x <= y  |
"""
print(comparison_table)

# Exzample of using comparison operators
print (3 == 4)  # False
print (3 != 4)  # True
print (3 > 4)   # False
print (3 < 4)   # True
print (3 >= 4)  # False
print (3 <= 4)  # True


# if Statements
# Used in conditionals to comapre values and run code based on the condition True or False
# syntax:
# if condition:
#     pass # code to run if condition is True
# if starement starts with the keyword "if" followed by a condition and a colon(:)
# pass is a placeholder for code that will run if the condition is True

# The code will only run if the condition is True, otherwise it will be skipped
example = 3
if example > 2:
    print("example is greater than 2")  # This will run because the condition is True
    
# Indentation is important in Python, as it indicates which code belongs to the if statement. 
# The code block under the if statement must be indented four spaces.
# IdentationError will occur if the code is not indented properly.
# age = 18
# if age >= 18:
# print("You are an adult.")  # IndentationError: expected an indented block after 'if' statement on line 3


# else Clause
# The else clause is used to run code when the condition in the if statement is False
condition = False
if condition == True:
    pass # code to run if condition is True
else:
    pass # code to run if condition is False


else_clause_example = 3
if else_clause_example > 4:
    print("else_clause_example is greater than 4")  # This will not run because the condition is False
else:
    print("else_clause_example is not greater than 4")  # This will run because the condition is False

# else clause cannot be placed before and between if statement, it must always come 
# after the if statement and.

# elif Cluases
# The elif clause is used to check multiple conditions in a single if statement
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
    
    


# Truthy and Falsy Values, Boolean Operators and Short-Circuiting
# nested conditionals are conditionals that are placed inside other conditionals.
is_citizen = True
age = 20
if is_citizen:
    if age >= 18:
        print("You are eligible to vote.") # You are eligible to vote
    else:
        print("You are not eligible to vote.")
else:
    print("You are not a citizen and cannot vote.")
    

# Truthy and Falsy Values
# In Python, certain values are considered "truthy" or "falsy" when used in a boolean context.
# Truthy values are values that evaluate to True in a boolean context, while falsy values
# bool() function can be used to check if a value is truthy or falsy
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

# Boolean Operators (and, or, not)

# The and operator
# The and operator takes two operands and returns the first operand if it is falsy; 
# otherwise, it returns the second operand. 
# Both operands must be truthy for an expression to result in a truthy value.
is_citizen = True
age = 25
print(is_citizen and age) # 25

# The number 25 is printed to the terminal because the and operator will evaluate the 
# second operand if the first operand is True. The and operator is known as a short-circuit operator. 
# Short-circuiting means Python checks values from left to right 
# and stops as soon as it determines the final result.
# example of using and instead of nested if statements
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print("You are eligible to vote.") # You are eligible to vote
else:
    print("You are not eligible to vote.")
# Example above evluates to True because both is_citizen and age >= 18 are True, 
# so the code block under the if statement runs.

# The or Operator
# The or operator takes two operands and returns the first operand if it is truthy;
# otherwise, it returns the second operand. 
# It is also short-circuit operator, it will stop evaluating as soon as it finds a truthy value.
age = 19
is_employed = False
print(age or is_employed) # 19
# The code will print number 19 because the first operand age is truthy, 
# so the or operator will not evaluate the second operand.
age = 19
is_student = True
if age < 18 or is_student:
    print("You are eligible for a student discount.") # You are eligible for a student discount
else:
    print("You are not eligible for a student discount.")
# age < 19 is False, but is_student is True, so the code block under the if statement runs.

# The not Operator
# The not operator takes a single operand and returns the opposite boolean value.
print(not '') # True, because empty string is falsy, so not operator returns True
print(not 'Hello') # False, because non-empty string is truthy, so not operator returns False
print(not 0) # True, because 0 is falsy, so not operator returns True
print(not 1) # False, because 1 is truthy, so not operator returns False
print(not True) # False, because True is truthy, so not operator returns False
print(not False) # True, because False is falsy, so not operator returns True

is_admin = False
if not is_admin:
    print("You do not have admin privileges.") # You do not have admin privileges
else:
    print("You have admin privileges.")
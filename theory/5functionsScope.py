# Functions
# Functions are reusable code that run when you call it

# built-in function input()
name = input('What is your name?') # User types "Kolade" and presses Enter  
print("Hello", name) # Output: Hello Kolade

# function int()
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 


# Defining and Calling Functions
# Writing custom functions using def keyword followed by the name of the function
# a pair of parantheses and colon. The on the new line wrie what should the function run
def hello():
    print('Hello World')

hello() #Hello World


# Parameters and Arguments
def calculate_sum(a, b):
    print(a + b)

# The function above has a and b inside its paranthese an those are parameters.
# Parameters are a placeholder varaibales that acts as "slots" for the values you
# pass into function when you call it.
# To use the parameters, you have to pass in "arguments".
# Arguments are the values you pass to a function when you call it.
calculate_sum(3, 1) #4

# If you call the function without the correct number of arguments, you will get a TypeError
# calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'


# Returning Values from Functions
# Functions use return keyword to exit the function and return a value.
# If the return keyword is not used, Python will return None by default
my_sum = calculate_sum(3, 1) #4
print(my_sum) # None

def calculate_sum(a, b):
    return a + b
my_sum = calculate_sum(3,1)
print(my_sum) #4

# By using return the function will returns the sum of a and b which gets stored in my_sum



# Scope
# Scope determines wher you can use a variable in your code.

# Global scope, variable created outside a function and can be use both inside and outside functions.

# Local scope, variable created inside a function. Only able to use inside that function.
# Function parameters are local variables too
# Example of local and global scope:
tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
# print(tax) # NameError: name 'tax' is not defined

# The tax_rate variable is global because it is created outside the function. The calculate_tax
# function can red it and the second pint() call can read it too.
# Howerver the price and the tax variable are local to calculate_tax. The are there while that function
# runs, but not outside and the reason it raises a NameError


# Theory Numbers and Mathematical Operations

# Integers and Floating Point Numbers

# Integers are whole numbers without decimal points
x = 5
y = -10
z = 0
print(type(x), "x:", x) # <class 'int'>
print(type(y), "y:", y) # <class 'int'>
print(type(z), "z:", z) # <class 'int'>

# Perform an addition operation on integers
sum_ints = x + y
print("\nSum of integers: x + y =", sum_ints) # Output: -5

# Perform a subtraction operation on integers
diff_ints = x - y
print("\nDifference of integers: x - y =", diff_ints) # Output: 15

# Perform a multiplication operation on integers
prod_ints = x * y
print("\nProduct of integers: x * y =", prod_ints) # Output: -50

# Perform a division operation on integers
div_ints = x / y
print("\nDivision of integers: x / y =", div_ints) # Output: -0.5

print("\n")


# Floating Point Numbers are positive or negative
# numbers with decimal points
a = 3.14
b = -2.5
c = 0.0
print(type(a), "a:", a) # <class 'float'>
print(type(b), "b:", b) # <class 'float'>  
print(type(c), "c:", c) # <class 'float'>

# Perform an addition operation on floating point numbers
float_addition = a + b
print("\nSum of floating point numbers: a + b =", float_addition) # Output: 0.64

# Perform a subtraction operation on floating point numbers
float_substraction = a - b
print("\nDifference of floating point numbers: a - b =", float_substraction) # Output: 5.64

# Perform a multiplication operation on floating point numbers
float_multiplication = a * b
print("\nProduct of floating point numbers: a * b =", float_multiplication) # Output: -7.85

# Perform a division operation on floating point numbers
float_division = a / b
print("\nDivision of floating point numbers: a / b =", float_division) # Output: -1.256

# Adding integer and float will convert the integer to float
sum_int_and_float = x + a
print("\nSum of integer and float: x + a =", sum_int_and_float) # Output: 8.14
print(type(sum_int_and_float), "sum_int_and_float:", sum_int_and_float) # <class 'float'>


# Modulus Operator % returns the remainder of a division operation
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print("\n" + f"Modulus of integers: {my_int_1} % {my_int_2} =", mod_ints) # Output: 8
print(f"Modulus of floats: {my_float_2} % {my_float_1} =", mod_floats) # Output: 1.2


# Floor Division Operator // returns the largest integer less than or equal to the division result
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print("\n" + f"Floor division of integers: {my_int_1} // {my_int_2} =", floor_div_ints) # Output: 4
print(f"Floor division of floats: {my_float_2} // {my_float_1} =", floor_div_floats) # Output: 2.0


# Exponentiation Operator ** raises a number to the power of another number
exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print("\n" + f"Exponentiation of integers: {my_int_1} ** {my_int_2} =", exp_ints) # Output: 56 ** 12
print(f"Exponentiation of floats: {my_float_1} ** {my_float_2} =", exp_floats) # Output: 5.4 ** 12.0


# float() function converts an integer to a floating point number
int_to_float = float(my_int_1)

print("\n" + f"Converting integer to float: float({my_int_1}) =", int_to_float) # Output: 56.0

# int() function converts a floating point number to an integer
float_to_int = int(my_float_1)
print(f"Converting float to integer: int({my_float_1}) =", float_to_int) # Output: 5

# round() function rounds a floating point number to the nearest integer
rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print("\n" + f"Rounding integer: round({my_int_1}) =", rounded_int_1) # Output: 56
print(f"Rounding float: round({my_int_2}, 1) =", rounded_int_2) # Output: 12.0

# abs() function returns the absolute value of a number
num = -15
abs_num = abs(num)

print("\n" + f"Absolute value of {num} is {abs_num}") # Output: Absolute value of -15 is 15

# pow() function raises a number to the power of another number
base = 2
exponent = 3
power_result = pow(base, exponent)

print("\n" + f"{base} raised to the power of {exponent} is {power_result}") # Output: 2 raised to the power of 3 is 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(f"2 raised to the power of 3 modulo 5 is {result_2}") # Output: 2 raised to the power of 3 modulo 5 is 3



# Augmented Assignment Operators
print("\nAugmented Assignment Operators:")

print("Addition augmented assignment operator (+=):")
aug_var = 10
aug_var += 5  # Equivalent to aug_var = aug_var + 5
print(f"After += operation, aug_var = {aug_var}") # Output: 15

aug_var = aug_var + 5
print(f"equivalent operation, aug_var = {aug_var}") # Output: 20

print ("\nSubtraction augmented assignment operator (-=):")
count = 14 
count -= 3  # Equivalent to count = count - 3
print(f"After -= operation, count = {count}") # Output: 11

print("\nMultiplication augmented assignment operator (*=):")
product = 65
product *= 7 # Equivalent to product = product * 7
print(f"After *= operation, product = {product}") # Output: 455

print("\nDivision augmented assignment operator (/=):")
price = 100
price /= 4 # Equivalent to price = price / 4
print(f"After /= operation, price = {price}") # Output: 25.0

print("\nFloor division augmented assignment operator (//=):")
total_pages = 23
total_pages //= 5  # Equivalent to total_pages = total_pages // 5
print(f"After //= operation, total_pages = {total_pages}") # Output: 4

print("\nModulus augmented assignment operator (%=):")
bits = 35
bits %= 2
print(f"After %= operation, bits = {bits}") # Output: 1

power = 2
power **= 3  # Equivalent to power = power ** 3
print(f"After **= operation, power = {power}") # Output: 8

print("\nAugmented assignment on string concatenation:")
message = "Hello, "
message += "World!"
print(f"After += operation, message = {message}") # Output: Hello, World!

print("\nAugmented multiplication on string:")
greet = 'Hello'
greet *= 3
print(f"After *= operation, greet = {greet}") # Output: HelloHelloHello         

print("Augmented subtraction and division on string is not possible as it will throw an error")
greet -= 'Hello' # This will throw an error
greet /= 2 # This will throw an error


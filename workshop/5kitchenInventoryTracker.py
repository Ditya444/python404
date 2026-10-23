# Build a Kitchen Inventory Tracker

# Step 1
# Define basic data for the kitchen inventory.
available_eggs = 1
available_flour = 2
available_sugar = 3

# Step 2
# Create a function to check kitchen current inventory.
def check_kitchen_stock():
    pass

# Step 3
# Replace the pass keyword with a new variable in the check_kitchen_stock funtion.
def check_kitchen_stock():
    total_items = available_flour + available_eggs + available_sugar

# Step 4
# Display the current inventory.
def check_kitchen_stock():
    total_items = available_flour + available_eggs + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')
    
# Step 5
# Try to execute the function by calling (or invoking) the function.
check_kitchen_stock()

# Step 6
# After checking the kitchen's stock, create a new function to check what stock could be used.
def use_eggs(available_eggs, eggs_to_use):
    pass
# Note that if you give a parameter the exact same name as a global variable 
# (like available_eggs), the function will use its own local parameter available_eggs 
# instead of the global one. 
# This is known as name shadowing since the local variable "shadows" the global one.

# Step 7
# Check if you have enough egss inside the use_eggs function.
def use_eggs(available_eggs, eggs_to_use):
    if available_eggs < eggs_to_use:
        print('The kitchen does not have enough eggs.')
        
# Step 8
# Prevent the function to run since there are not enough egss to cook and return the number of eggs
def use_eggs(available_eggs, eggs_to_use):
    if available_eggs < eggs_to_use:
        print('The kitchen does not have enough eggs.')
        return available_eggs

# Step 9
# Add another condition if the first condition evaluates to false and check the remaining eggs after used
def use_eggs(available_eggs, eggs_to_use):
    if available_eggs < eggs_to_use:
        print('The kitchen does not have enough eggs.')
        return available_eggs
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

# Step 10
# Call the use_eggs function and pass two arguments: the global availanle_eggs
# variabe and the number 1 (respresent number of eggs you want to use)
use_eggs(available_eggs, 1)

# Step 11
# Check how many available_eggs variable left, and the output is still 1
print(available_eggs)

# Step 12
# To solve step 11 problem create a new function. Think of it as your
# recipe, a function that calls other function.
def make_fried_egg(available_eggs):
    pass

# Step 13
# Before cooking the fried egg, its better to check if we have the
# required ingredients. Do this by comparing the value of availaibe
# eggs with the amount needed to fried.
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    
# Step 14
# In step 11, when the use_eggs function returned the number, it did not
# save the value. To update the inventory, capture that returned value by
# assigning it to a variable. 
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")

# Step 15
# The new updated make_fried_egg function now checks whether an egg
# is available and updates its local egg count when one is used. 
# Next is to return that counst so the caller can use it.
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")
    return available_eggs

# Step 16
# When a function returns a value, it does not overwerite the exising
# variables. You must explicitly save that new value so it will not have 
# a problem like in step 11. The available_eggs variable inside the make_fried_egg
# function, it is not the same variable defined at the top of the code.
# The one inside the function is a local variable. When the function endss,
# the local variable is discarded, and the global available_eggs
# remians unchanged. Therefore update the actual kitchen inventory by
# overwrite the global available_eggs variable with the number returned
# by make_fried_egg function.
available_eggs = make_fried_egg(available_eggs)

# Step 17
# Verify the kitchen inventory that the number of eggs has decreased.
check_kitchen_stock()

# Final code
available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

available_eggs = make_fried_egg(available_eggs)

check_kitchen_stock()
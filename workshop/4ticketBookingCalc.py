# Movie Ticket Booking Calculator

# Step 1
# Declaring variables that store information about the user and the movie show
base_price = 15
age = 21

# Step 2
# Variable that stores string values about movie ticket
seat_type = 'Gold'
show_time = 'Evening'

# Step 3
# Eligibility check for ticket booking based on age
if age > 17:
    print("User is eligible to book a ticket.")
    
# Step 4
# Check if user is allowed to book an evening show based on age
if age >= 21:
    print("User is eligible for Evening shows")
    
# Step 5
# Adding an else statement to handle cases where the user is not eligible for evening shows
if age >= 21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")

# Step 6
# Variable for member user status and weekend show status
is_member = True
is_weekend = False

# Step 7
# Variable for discount
discount = 0

# Step 8
# if statement to check if is_member is truthy
if is_member:
    discount = 3
    print('User qualifies for membership discount')
    
# Step 9 
# Check if the user does not qualify for membership discount
if is_member:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Step 10
# Update the condition for membership discount using and operator
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Step 11
# Check when the value of the is_member is False
is_member = False
discount = 0 
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Step 12
# Add a variable for extra charges applied for weekend shows
extra_charges = 0
if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')

# Step 13
# Add an else clause check if no extra charges and show the updated value
extra_charges = 0
if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Step 14
# Use or operator to combine the existing condition with a second condition if 
# show is equal to string 'Evening'
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Step 15
# Create an if statement if the user satisfies the booking condition
if age >= 21:
    print("Ticket booking condition satisfied")
else:
    print('Ticket booking failed due to restrictions')

# Step 16
# Create a specific conditon that user between 18 to 21 can book when is not evening
if age >= 21 or age >= 18 and show_time != 'Evening':
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
    
# Step 17
# Adding an exception of someone is a member who are 18 - 21 can book evening shows
# When using multiple logical operators in an if statement, and some operator has a 
# higher precedence than other. You can use the parantheses () to change how conditions are grouped
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
    
# Step 18 and 19
# Add nested if that calculate service charges based on the type of seat
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    else:
        service_charges = 1
else:
    print('Ticket booking failed due to restrictions')
    
# Step 20
# Add an elif clause to calculate service charges based on the type of seat
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)
else:
    print('Ticket booking failed due to restrictions')

# Step 21
# Calculate the final price by adding the extra charges and service charges to the base price
# then subtracting the discount
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
else:
    print('Ticket booking failed due to restrictions')
    
# Final look at the code
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    
else:
    print('Ticket booking failed due to restrictions')
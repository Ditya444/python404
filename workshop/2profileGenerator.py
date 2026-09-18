# Employee Profile Generator

# Step 1: Creating a variable for first name and last name
first_name = "John"
last_name = "Doe"

print("Step 1: Creating a variable for first name and last name")
print(first_name)
print(last_name)

print("\n")  # Adding a newline for better readability

# Step 2 and 3: Combining strings using concatenation + and using space
full_name = first_name + " " + last_name

print("Step 2 and 3: Combining strings using concatenation + and using space")
print(full_name)

print("\n")  # Adding a newline for better readability

# Step 4: Creat a variable address
address = "123 Main Streeet"

print("Step 4: Create a variable address")
print(address)

print("\n")  # Adding a newline for better readability

# Step 5: Augmented assignment operator to add a string to the address variable
address += ", Apartment 4B"

print("Step 5: Augmented assignment operator to add a string to the address variable")
print(address)

print("\n")  # Adding a newline for better readability

# Step 6 and 7: Create a variable for employee age
employee_age = 28

print("Step 6 and 7: Create a variable for employee age")
print(employee_age)

print("\n")  # Adding a newline for better readability

# Step 8 and 9: Employee info and try o concatenate a string with a number
# employee_info = full_name + " is " + employee_age
# print(employee_info)  # This will raise a TypeError

print("\n")  # Adding a newline for better readability

# Step 10: Fix the TypeError by converting the number into a string with str() function
# employee_info = full_name + " is " + str(employee_age)

# Step 11 Completing the employee profile with all the information
employee_info = full_name + " is " + str(employee_age) + " years old"
print("Step 11: Completing the employee profile with all the information")
print(employee_info)

print("\n")  # Adding a newline for better readability

# Step 12: Use str() function to convert numbers to strings and ad variable
# experience_years and contenate it to the experience_info variable
experience_years = 5
experience_info = "Experience: " + str(experience_years) + " years"
print("Step 12: Displaying employee experience information")
print(experience_info)

print("\n")  # Adding a newline for better readability

# Step 13: Use f-strings to create a formatted string for the employee_card
employee_card = f'Employee {full_name}'
print("Step 13: Use f-strings to create a formatted string for the employee_card")
print(employee_card)

print("\n")  # Adding a newline for better readability

# Step 14: Use f-strings to create a formatted string for the employee_card with
# more information
employee_card = f'Employee: {full_name} | Age: {employee_age}'
print("Step 14: Use f-strings to create a formatted string for the employee_card with more information")
print(employee_card)

print("\n")  # Adding a newline for better readability

# Step 15: Use f-strings to create a formatted string for the employee_card with updated information
position = "Data Analyst"
salary = 75000
employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}."

print("Step 15: Use f-strings to create a formatted string for the employee_card with updated information")
print(employee_card)

print("\n")  # Adding a newline for better readability

# Step 16: Slicing the employee_card string to extract specific information
employee_code = "DEV-2026-JD-001"
department = employee_code[0:3]  # Extracting the department code
print("Step 16: Slicing the employee_card string to extract specific information")
print(f"Department Code: {department}")

print("\n")  # Adding a newline for better readability

# Step 17: Slicing the employee_card strinng from the middle to the end to extract the employee ID
year_code = employee_code[4:8]  # Extracting the year code
initials = employee_code[9:11]  # Extracting the initials
print("Step 17: Slicing the employee_card string from the middle to the end to extract the employee ID")
print(f"Year Code: {year_code}, Initials: {initials}")

print("\n")  # Adding a newline for better readability

# step 18: Slicing the employee_card string from the end to extract the unique identifier
last_three = employee_code[-3:]  # Extracting the last three characters
print("Step 18: Slicing the employee_card string from the end to extract the unique identifier")
print(f"Unique Identifier: {last_three}")

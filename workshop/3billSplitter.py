# Build Splitter
# Calculate how much each person owes after adding meal costs and a tip

# Step 1: keep track of the total amount as costs are added 
running_total = 0

# Step 2: account of the number of people sharing the bill
num_of_friends = 4

#  Step 3: cost for each course of the meal in cents
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Step 4: calculate the total cost of the meal
running_total += appetizers + main_courses + desserts + drinks
print(f"Total bill so far: {running_total}")

# Step 5: calculate the tip amount (25% of the total bill)
tip = running_total * 0.25
print(f"Tip amount: {tip}")

# Step 6: final total after adding the tip
running_total += tip
print(f"Final total after tip: {running_total}")

# Step 7: calculate how much each person owes
final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

# Step 8: round the final bill to two decimal places
each_pays = round(final_bill, 2)
print(f"Each person pays: {each_pays}")



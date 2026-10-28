# Build an Apply Discount Function
# Calculate the final price of an item after applying a percentage discount

# User Stories:
# 1. Define a function named apply_discount.
# 2. The function abouce take two parameters: price and discount.
# 3. If parameter price is not int or float, the function should.
# return the string "The discount should be a number".
# 4. If discount is not a number, the function should 
# return the string "The discount should be a number".
# 5. If price is less than or equal to 0, the function should
# return the string "The discount should be between 0 and 100".
# 6. If discount is less than 0 or greater than 100, the function
# should return the string "The discount should be between 0 and 100".
# 7. If both inputs are valid, the function should calculate the discount
# as a percentage of the price.
# 8. The function should return the final price after applying the discount.

def apply_discount(price, discount):
    final_price = 0
    
    if not isinstance(price, (int, float)):
        return f"The price should be a number"
    if not isinstance(discount, (int, float)):
        return f"The discount should be a number"
    
    if price <= 0:
        return f"The price should be greater than 0"
    if discount < 0 or discount > 100:
        return f"The discount should be between 0 and 100"
    
    final_price = (100 - discount) / 100 * price
    
    return final_price

print(apply_discount("test", "duar"))
print(apply_discount(40, "duar"))
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(100, 100))
print(apply_discount(74.5, 20.0))






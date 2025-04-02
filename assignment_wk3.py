def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount to the original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price
print(calculate_discount(100, 20))  # Should return 80.0

# Prompt the user for the original price and discount percentage
price = float(input("100: $"))
discount_percent = float(input("20%: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == price:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
else:
    print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")

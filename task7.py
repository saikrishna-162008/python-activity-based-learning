
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    price = float(input("Enter price per item: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity")
        continue

    amount = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 8
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 10

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    print("Product:", name)
    print("Amount: Rs.", round(amount, 2))
    print("Tax Rate:", tax_rate, "%")
    print("Tax: Rs.", round(tax, 2))

# Threshold-based discount
if subtotal >= 10000:
    discount_rate = 15
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 1500
discount = min(discount, max_discount)

final_bill = subtotal + total_tax - discount

# Itemized invoice
print("\n================================")
print("          RETAIL INVOICE")
print("================================")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount Rate  :", discount_rate, "%")
print("Discount       : Rs.", round(discount, 2))
print("--------------------------------")
print("Final Bill     : Rs.", round(final_bill, 2))
print("================================")

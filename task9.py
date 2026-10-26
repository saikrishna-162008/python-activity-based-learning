
print("=== Multi-Currency Travel Budget Analysis ===")

budget = float(input("Enter total travel budget in INR: Rs. "))
fee_percent = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expenses: "))

expenses = []
total_spending = 0

for i in range(n):
    print(f"\nExpense {i + 1}")

    category = input("Enter category (Food/Travel/Hotel/Shopping): ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code (INR/USD/EUR): ").upper()
    rate = float(input("Enter exchange rate in INR: "))

    if amount < 0 or rate <= 0:
        print("Invalid amount or exchange rate!")
        continue

    converted = amount * rate
    fee = converted * fee_percent / 100
    final_amount = converted + fee

    expenses.append({
        "category": category,
        "currency": currency,
        "original": amount,
        "converted": converted,
        "fee": fee,
        "total": final_amount
    })

    total_spending += final_amount

print("\n========== TRAVEL EXPENSE REPORT ==========")

category_totals = {}

for e in expenses:
    print(f"\nCategory: {e['category']}")
    print(f"Original Amount: {e['original']:.2f} {e['currency']}")
    print(f"Converted Amount: Rs. {e['converted']:.2f}")
    print(f"Conversion Fee: Rs. {e['fee']:.2f}")
    print(f"Total Expense: Rs. {e['total']:.2f}")

    category_totals[e["category"]] = (
        category_totals.get(e["category"], 0) + e["total"]
    )

print("\nTotal Spending: Rs.", round(total_spending, 2))
print("Travel Budget: Rs.", round(budget, 2))
print("Remaining Budget: Rs.", round(budget - total_spending, 2))

if total_spending > budget:
    print("Status: Budget Exceeded!")
else:
    print("Status: Within Budget.")

if category_totals:
    largest = max(category_totals, key=category_totals.get)
    print("Largest Expense Category:", largest)
    print("Category Total: Rs.", round(category_totals[largest], 2))

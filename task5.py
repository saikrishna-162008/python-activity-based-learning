
# Multi-Plan Telecommunications Cost Optimization

data = [
    ["Plan A", 199, 28, 2, 100, 1],
    ["Plan B", 299, 56, 3, 200, 0.5],
    ["Plan C", 399, 84, 4, 300, 0.25]
]

data_gb = float(input("Enter monthly data usage (GB): "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

eligible_plans = []

print("\n--- Plan Comparison ---")

for plan in data:
    name, price, days, included_gb, extra_rate, unused = plan

    excess_data = max(0, data_gb - included_gb)
    excess_charge = excess_data * extra_rate
    total_cost = price + excess_charge

    eligible = days >= validity and total_cost <= budget

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Validity:", days, "days")
    print("Excess Data:", excess_data, "GB")
    print("Excess Charge: Rs.", round(excess_charge, 2))
    print("Total Cost: Rs.", round(total_cost, 2))
    print("Eligible:", "Yes" if eligible else "No")

    if eligible:
        eligible_plans.append((name, total_cost))

print("\n--- Best Plan ---")

if eligible_plans:
    best = min(eligible_plans, key=lambda x: x[1])
    print("Most Economical Plan:", best[0])
    print("Total Cost: Rs.", round(best[1], 2))
else:
    print("No plan satisfies the budget and validity constraints.")

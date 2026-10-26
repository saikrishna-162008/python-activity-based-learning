
# Progressive Electricity Billing Analysis

months = ["January", "February", "March", "April"]
units_list = [120, 180, 260, 400]

fixed_charge = 50
surcharge_rate = 0.05
rebate_rate = 0.10

bills = []

for i in range(len(months)):
    units = units_list[i]

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        energy_charge = (
            100 * 2 + 100 * 3 + 100 * 5
            + (units - 300) * 7
        )

    surcharge = energy_charge * surcharge_rate
    rebate = energy_charge * rebate_rate

    total_bill = (
        energy_charge + fixed_charge
        + surcharge - rebate
    )

    bills.append(total_bill)

    print("\nMonth:", months[i])
    print("Units Consumed:", units)
    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total_bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(len(months)):
    print(months[i], ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]
        percentage = (increase / bills[i - 1]) * 100

        if percentage > 30:
            print("WARNING: Unusual bill increase!")
        elif increase > 0:
            print("Bill increased by Rs.", round(increase, 2))
        else:
            print("Bill decreased or remained same.")

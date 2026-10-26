
# Manufacturing Cost and Profitability Analysis

product = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour cost per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost: "))
selling_price = float(input("Enter selling price per unit: "))
profit_target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material_cost < 0 or labour_cost < 0
        or machine_cost < 0 or selling_price < 0
        or not 0 <= wastage_percent <= 100
        or profit_target < 0):

    print("Invalid input values")

else:
    material_total = material_cost * quantity
    wastage_cost = material_total * wastage_percent / 100
    labour_total = labour_cost * quantity

    total_cost = (
        material_total + wastage_cost
        + labour_total + machine_cost
    )

    total_revenue = selling_price * quantity
    profit = total_revenue - total_cost

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    print("\n===== MANUFACTURING REPORT =====")
    print("Product Name:", product)
    print("Production Quantity:", quantity)
    print("Material Cost: Rs.", round(material_total, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(labour_total, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue: Rs.", round(total_revenue, 2))
    print("Net Profit/Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit >= 0 and profit_percent >= profit_target:
        print("Status: Profit target achieved")
    else:
        print("Status: Profit target not achieved")

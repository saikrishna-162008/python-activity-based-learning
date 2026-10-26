
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

total_fare = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("1. Sleeper")
    print("2. AC")
    print("3. First Class")
    travel_class = int(input("Select travel class: "))

    # Distance-based fare
    if distance <= 100:
        base_fare = distance * 1
    elif distance <= 500:
        base_fare = 100 * 1 + (distance - 100) * 1.5
    else:
        base_fare = 100 + 400 * 1.5 + (distance - 500) * 2

    # Class charges
    if travel_class == 1:
        class_charge = 50
    elif travel_class == 2:
        class_charge = 200
    elif travel_class == 3:
        class_charge = 400
    else:
        print("Invalid class. Using Sleeper.")
        class_charge = 50

    # Age-based concession (sample policy)
    if age < 5:
        concession = base_fare
    elif age >= 60:
        concession = base_fare * 0.20
    else:
        concession = 0

    reservation_fee = 40

    fare = base_fare + class_charge + reservation_fee - concession

    print("\nPassenger Name:", name)
    print("Base Fare: Rs.", round(base_fare, 2))
    print("Class Charge: Rs.", class_charge)
    print("Reservation Fee: Rs.", reservation_fee)
    print("Concession: Rs.", round(concession, 2))
    print("Final Fare: Rs.", round(fare, 2))

    total_fare += fare

print("\nTotal Reservation Fare: Rs.", round(total_fare, 2))

# Cancellation calculation
cancel = input("\nDo you want to calculate cancellation? (yes/no): ")

if cancel.lower() == "yes":
    penalty_rate = float(input("Enter cancellation penalty percentage: "))

    if 0 <= penalty_rate <= 100:
        penalty = total_fare * penalty_rate / 100
        refund = total_fare - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))
    else:
        print("Invalid penalty percentage.")

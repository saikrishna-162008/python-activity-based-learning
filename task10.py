
import math

print("=== Campus Event Financial Planning ===")

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering_per_person = float(input("Enter catering cost per person: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate_per_person = float(input("Enter certificate cost per person: Rs. "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
registration_fee = float(input("Enter registration fee per person: Rs. "))

if (min(venue, equipment, catering_per_person, transport,
        certificate_per_person, sponsorship, registration_fee) < 0
        or participants < 0):
    print("Invalid input! Values cannot be negative.")

else:
    fixed_cost = venue + equipment + transport

    variable_cost = (
        catering_per_person + certificate_per_person
    )

    total_cost = fixed_cost + variable_cost * participants

    participant_contribution = registration_fee * participants

    total_funds = participant_contribution + sponsorship

    shortfall = max(0, total_cost - total_funds)

    print("\n========== EVENT BUDGET REPORT ==========")
    print(f"Venue Cost: Rs. {venue:.2f}")
    print(f"Equipment Cost: Rs. {equipment:.2f}")
    print(f"Catering Cost: Rs. {catering_per_person * participants:.2f}")
    print(f"Transport Cost: Rs. {transport:.2f}")
    print(f"Certificate Cost: Rs. {certificate_per_person * participants:.2f}")
    print(f"Total Event Cost: Rs. {total_cost:.2f}")
    print(f"Participant Contributions: Rs. {participant_contribution:.2f}")
    print(f"Sponsorship: Rs. {sponsorship:.2f}")
    print(f"Sponsorship Shortfall: Rs. {shortfall:.2f}")

    if total_funds >= total_cost:
        print("Status: Event Budget Covered")
    else:
        print("Status: Additional Funds Required")

    # Break-even registration count
    contribution_per_person = registration_fee - variable_cost
    remaining_fixed_cost = fixed_cost - sponsorship

    if remaining_fixed_cost <= 0:
        break_even = 0
    elif contribution_per_person > 0:
        break_even = math.ceil(
            remaining_fixed_cost / contribution_per_person
        )
    else:
        break_even = None

    if break_even is not None:
        print("Minimum Break-even Registrations:", break_even)
    else:
        print("Break-even is not possible at this registration fee.")

    print("==========================================")

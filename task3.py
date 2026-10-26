
# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing constraints
if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid patient details or billing charges")

else:
    total = consultation + diagnostic + treatment

    # Conditional concessions
    if age >= 60:
        concession_rate = 20
    elif total >= 10000:
        concession_rate = 10
    else:
        concession_rate = 0

    concession = total * concession_rate / 100
    final_bill = total - concession

    # Payment policy
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Age:", age)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Charges: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)

    if final_bill < 2000:
        category = "Low Payment"
    elif final_bill <= 10000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("Patient Classification:", category)

    payment = float(input("Enter amount paid: "))

    if payment < 0:
        print("Invalid payment amount")
    elif payment > final_bill:
        print("Overpayment: Rs.", payment - final_bill)
    elif payment == final_bill:
        print("Payment Status: Fully Paid")
    else:
        print("Payment Status: Partially Paid")
        print("Balance Due: Rs.", final_bill - payment)

annual_income = float(input("Enter your annual income: ₹"))
residency_status = input("Enter your residency status (Resident/Non-Resident): ")
if annual_income <= 30000:
    tax_rate = 0.0
elif annual_income <= 80000:
    if residency_status.lower() == "resident":
        tax_rate = 0.10
    else:
        tax_rate = 0.15
else:
    tax_rate = 0.25
tax_amount = annual_income * tax_rate
remaining_balance = annual_income - tax_amount
print("\n" + "="*50)
print("TAX CALCULATION SUMMARY")
print("="*50)
print(f"Annual Income:      ₹{annual_income:,.2f}")
print(f"Residency Status:   {residency_status}")
print(f"Tax Rate Applied:   {tax_rate * 100:.1f}%")
print(f"Tax Amount:         ₹{tax_amount:,.2f}")
print(f"Remaining Balance:  ₹{remaining_balance:,.2f}")
print("="*50)
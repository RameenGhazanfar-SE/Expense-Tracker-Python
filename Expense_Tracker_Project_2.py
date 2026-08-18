# ==========================================
#        EXPENSE TRACKER
#        DecodeLabs - Project 2
# ==========================================

print("=" * 40)
print("          EXPENSE TRACKER")
print("=" * 40)

total_spent = 0
expense_count = 0

print("\nEnter your expenses one by one.")
print("Enter 0 when you are finished.\n")

while True:
    try:
        expense = float(input("Enter expense amount: "))

        if expense < 0:
            print("Please enter a positive amount.")
            continue

        if expense == 0:
            break

        total_spent += expense
        expense_count += 1

        print(f"Expense added: {expense:.2f}")
        print(f"Current total: {total_spent:.2f}\n")

    except ValueError:
        print("Invalid input. Please enter a number.\n")

print("=" * 40)
print("           EXPENSE SUMMARY")
print("=" * 40)
print(f"Number of expenses: {expense_count}")
print(f"Total Spent:        {total_spent:.2f}")
print("=" * 40)
print("Thank you for using Expense Tracker!")

print("===weekly expenses===")
name = input("Enter student name: ")
while True:
    try:
        budget = float(input("Enter weekly budget: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for the budget.")

print("==================================================")
print("\nCategories:")
print("1. Food                  [e.g. Lunch, snacks, coffee]")
print("2. Transport             [e.g. Bus, jeepney, ride-share]")
print("3. Mobile / internet     [e.g. Load, data plan, WiFi top-up]")
print("4. School  supplies      [e.g. Notebook, pen, bond paper]")
print("5. Entertainment         [e.g. Games, movies, hangout]")
print("==================================================")

logged_expenses = "" 
total_spent = 0
entry_count = 1

while entry_count <= 4:
    print("\nEntry #" + str(entry_count))
    choice = int(input("Enter category number (1-5, or 0 to skip): "))
    
    category_name = ""
    if choice == 0:
        print("Slot skipped.")
        category_name = "SKIP"
    elif choice == 1:
        category_name = "Food"
    elif choice == 2:
        category_name = "Transportation"
    elif choice == 3:
        category_name = "Mobile / internet"
    elif choice == 4:
        category_name = "School  supplies"
    elif choice == 5:
        category_name = "Entertainment"
    else:
        print("Invalid choice.")
        category_name = "SKIP"
    if category_name != "SKIP":
        desc = input("Item description: ")
        amt = float(input("Amount spent: "))

    alert = ""
    if amt > (budget * 0.25):
        alert = "! High Expense Alert!"
        
        logged_expenses += str(entry_count) + ". " + category_name + " (" + desc + "): $" + str(amt) + " " + alert + "\n"
        total_spent = total_spent + amt
        
    entry_count = entry_count + 1

remaining = budget - total_spent
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."


print("\n--- FINAL EXPENSE LOG ---")
print("Student Name: " + name)
print("Weekly Budget: $" + str(budget))
print("-------------------------")
print(logged_expenses)
print("-------------------------")
print("Total Spent: $" + str(total_spent))
print("Remaining Balance: $" + str(remaining))
print("Status: " + status)

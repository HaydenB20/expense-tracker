import json
from datetime import datetime

# Initialize the expense list
expenses = []

# Load expenses from a file
def load_expenses(filename="expenses.json"):
    global expenses
    try:
        with open(filename, "r") as file:
            expenses = json.load(file)
            print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No existing data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Corrupted data file. Starting fresh.")

# Save expenses to a file
def save_expenses(filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

# Add a new expense
def add_expense():
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f}")

# Get a summary by category
def get_summary():
    if not expenses:
        print("No expenses recorded.")
        return
    summary = {}
    for expense in expenses:
        summary[expense["category"]] = summary.get(expense["category"], 0) + expense["amount"]
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

# Main menu
def main():
    load_expenses()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            get_summary()
        elif choice == "4":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

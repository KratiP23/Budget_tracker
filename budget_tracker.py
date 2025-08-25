import os

# store transactions in a list
transactions = []

# load data from file if it exists
def load_transactions():
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3:   # at least type, amount, category must be there
                    t_type = parts[0]
                    amount = parts[1]
                    category = parts[2]
                    notes = parts[3] if len(parts) == 4 else "" 
                    transactions.append([t_type, float(amount), category, notes])

# save data to file
def save_transactions():
    with open("transactions.txt", "w") as f:
        for t in transactions:
            f.write(f"{t[0]},{t[1]},{t[2]},{t[3]}\n")

# add transaction
def add_transaction():
    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    notes = input("Enter notes (optional): ")
    transactions.append([t_type, amount, category, notes])
    print("Transaction added!\n")

# list all transactions
def list_transactions():
    if not transactions:
        print("No transactions yet.\n")
        return
    print("\nAll Transactions:")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t[0]} - {t[1]} - {t[2]} - {t[3]}")
    print()

# filter by type or category
def filter_transactions():
    choice = input("Filter by type or category? ").lower()
    if choice == "type":
        t_type = input("Enter type (income/expense): ").lower()
        for t in transactions:
            if t[0] == t_type:
                print(f"{t[0]} - {t[1]} - {t[2]} - {t[3]}")
    elif choice == "category":
        cat = input("Enter category: ").lower()
        for t in transactions:
            if t[2].lower() == cat:
                print(f"{t[0]} - {t[1]} - {t[2]} - {t[3]}")
    print() 

# show summary
def show_summary():
    income = sum(t[1] for t in transactions if t[0] == "income")
    expense = sum(t[1] for t in transactions if t[0] == "expense")
    print("\nSummary:")
    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Net Balance  :", income - expense, "\n")

# main program loop
def main():
    load_transactions()
    while True:
        print("==== Budget Tracker ====")
        print("1. Add transaction")
        print("2. List all transactions")
        print("3. Filter Transactions")
        print("4. Show summary")
        print("5. Save and Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            filter_transactions()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            save_transactions()
            print("Saved")
            break
        else:
            print("Invalid choice. Choose between 1-5")

main()

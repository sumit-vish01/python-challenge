#Personal Expense Tracker

Expense = []


#Add expense

def add_expense():

    print("\n-----ADD EXPENSE-----")

    name = input("Enter items name : ")
    price = float(input("Enter  item price: "))
    quantity = int(input("Enter  quantity: "))
    category = input("Enter category: ")


    total = price * quantity

        # Expense = {
        #         {"name" : "Lunch", "amount" : 80, "category":"Food"},
        #         {"name" : "bus", "amount" : 40, "category":"Travel"},
        #         {"name" : "Notebook", "amount" : 120, "category":"Study"}   
        # }

    expense = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total,
        "Category": Category
    }

    expense.append(expense)
    print("Expense added succesfully--")

def view_expense():

    print("\n----ALL EXPENSE-----")

    if len(Expense) == 0:
        print("NO expense found.")
        return

    
    for i , Expense in enumerate(Expenses, start=1):

        print(f"\nExpense {i}")
        print("Name:", Expense["name"])
        print("Price: $", Expense["Price"])
        print("Quantity:", Expense["Quantity"])
        print("Total:",Expense["total"])
        print("category:",Expense["category"])  

    

def total_expense():
    total = 0

    for Expense in Expense:
        total = total + Expense["total"]

    print("\n----TOTAL EXPENSE-----")
    print("Your total expense is: ", total)



while True:
    print("-------===== PERSONAL EXPENSE TRACKER =====--------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = int(input("Choose the number btw (1-4): "))


    if choice ==1:
       add_expense()

    elif choice == 2:
        view_expense()

    elif choice == 3:
        total_expense()

    elif choice == 4:
        highest_expense()

    elif choice == 5:
        search_expense()

    elif choice == 6:
        delete_expense()
    
    elif choice == 7:
        print("Thank you for using Expense Tracker!")

    else:
        print("X Invalid choice.")
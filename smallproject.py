# today i am making shopping cart
#shopping cart 

cart = [
    ["apple", 3,50],
    ["milk", 2, 100],
    ["egg", 4, 15],
    ["bread", 2,18],
    ["pizza", 100,20000]
]


print("----- welcome to your python shopping cart!------")

def add_items():
    item = input("Enter items: ")
    quantity = int(input("enter ur quantity: "))
    price = float(input("Enter price: "))
    found = False

    for product in cart:
        if product[0].lower() == item.lower():
            product[1] += quantity
            found = True
            print(f"{item} quantity updated!")
            break
    
    if not found:

       cart.append([item, quantity, price])

       item_total = quantity * price

       print(f"{item} * {quantity} = {item_total} added to your cart.")

def view_cart():
        if len(cart) == 0:
            print("Your currently cart is empty!.")

        else:
            print("\n-----Your Cart -----")
            total = 0
            for product in cart:
                item =product[0]
                quantity = product[1]
                price = product[2]

                item_total = quantity * price

                print(f"{item} * {product} = {item_total}") 

                total += item_total
            print(f"total = {total}")

def remove_cart():
    if len(car) ==0:
        print("Your cart is empty1")
        return
    item_to_remove = input("Enter item  u want remove: ")

    found = False

    for product in cart:
        if product[0] == item_to_remove:
            cart.remove(product)
            found = True

            print(f"{item_to_remove} removed from your cart.")
            break

        if not found:
            print(f"{item_to_remove} not found in your cart.")

def clear_cart():
        cart.clear()
        print("ur cart has been cleared.")


def checkout_and_exit():
    if len(cart) ==0:
        print("Your cart is empty")
        return

        print("\n------checkout-----")

        total = 0

        for product in cart:
            item =product[0]
            quantity = product[1]
            price = product[2]

            item_total = quantity * price

            print(f"{item} * {product} = {item_total}") 

            total += item_total

        print(f"\nOriginal Total = ${total}")

        coupon = input("Enter coupon code: ").upper()

        if coupon =="SAVE10":
            discount = total * 0.10

        elif coupon == "SAVE20":
            discount = total *0.20

        else:
            discount = 0
            print("Invalid coupon or no discount applied.")
        
        final_total = total - discount
        
        
        print(f"discount =${discount}")
        print(f"final_total = {final_total}")
        print("Thank you for shopping with us!")

#main program

while True:
    print("\nWould you like to add in your cart")
    print("1. Add items")
    print("2. view cart")
    print("3. remove cart")
    print("4. clear cart")
    print("5. checkout and exit ")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_items()

    elif choice == 2:
        view_cart()

    elif choice == 3:
        remove_cart()

    elif choice == 4:
        clear_cart()

    elif choice == 5:
        checkout_and_exit()
        break

    else:
        print("Invalid choice! please enter 1-5.")

        
    


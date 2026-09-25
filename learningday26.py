# class student:


#     def __init__(self):
#         self.name = "SUMIT"  #public
#         self._branch  = "CSE"#protected convention
#         self.__marks = 90 #private name-mangling

    
#getter/setter with property

# class student:
#     def __init__(self, marks):
#         self._marks = marks 


#     @property
#     def marks(self):
#         return self._marks

#     @marks.setter
#     def marks(self, value):
#         if 0<= value <= 100:
#             self._marks = value
#         else:
#             raise ValueError("Invalid marks")

#inheritance
# class Animal:
#     def speak(self):
#         print("Animal speak")


# class dog(Animal):
#     pass

#method overriding

# class animal:
#     def speak(self):
#         print("Animal sound")


# class dog(animal):
#     def speak(self):
#         print("bark")

# class animal:
#     def make_sound(self):
#         print("Janwar koi aawaz nikal rha hai..")


# class dog(animal):
#         def make_sound(self):
#             print("Kutta bhomk rha hai: BHOOQ~ BHOOW! ")

# class cat(animal):
#      def make_sound(self):
#         print("BILLI aawaz nikal rhai ha: mwaw meow! meow!")

# animal = animal()
# animal.make_sound()

# dog = dog()
# dog.make_sound()

# cat = cat()
# cat.make_sound()

# class employee:
#     def get_salary(self):
#         return 20000

# class manager(employee):
#     def get_salary(self):
#        base_salary = super().get_salary()
#        bonus = 5000
#        return base_salary + bonus


# mgr = manager()
# print(mgr.get_salary())

# #super methdos

# class animal:
#     def __init__(self, name):
#         self.name = name

# class dog(animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# ATM Simulation

pin = input("Enter your PIN: ") 

if pin == "1234":
    print("Login succesfull")


    Balance = 100000

    while True:
       print("\n -----ATM  MENU------")
       print("1. Check Balance")
       print("2. Deposit")
       print("3. Withdraw")
       print("4. Exit")


# amount = int(input("Enter deposit amount"))
# Balance =  Balance + amount

# if 2 > amount:
#    print("balance  + deposit_amount")
       choice = input("Enter your choice: ")

       if choice  ==  "1":
             print("Your balance is:", Balance)

        #depost
       elif choice  == "2":
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                  Balance = Balance + amount
                  print("DEposited amount succfully")
                  print("Your new balance is:", Balance)

            else:
                  print("Please enter a vaild amount")


       elif choice == "3":
             amount = int(input("Enter your withdraw amount: "))

             if amount > 0:
                  if amount <= Balance:
                      Balance = Balance - amount
                      print("Withdraw succesfully completed")
                      print("Your current balance is:", Balance)
                  else:
                    print("Insufficient amount please enter sufficient amount.")
             else:
                 print("Please enter a valid amount")
          #exit
       elif choice == "4":
            print("Thanking for choosing")
            break
       else:
            print("Invalid choice. please select 1-4.")


else:
  print("Wrong pin")


             


base_price = 13
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price - discount + extra_charges + service_charges
    print('Final price of ticket:',final_price)
else:
    print('Ticket booking failed due to restrictions')

import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["Rock" "paper" "scissors"]:
        continue

    random_number = random.randint(0,2)



print("good bye!")

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

        
    


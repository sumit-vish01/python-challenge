#zero to hero learning

# score = 85

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade:B")

# else:
#     print("Grade: C or below")

""" int(10, 5, -4), float(0.39), str("hellp world"), bool(True, False), type interaction 
and input type(that u want to type like anyword that u love to write)
"""

# age = input("Enter your age: ")
# age_as_int = int("age")
# print(type(age_as_int))

"""
operatores  + addition, subtraction, *multiplication, / division, //floor division, %modulus, ** exponentiation- power
comparison operators(==(equal to), !=(not equal to), > (greater than), <(less than), >=(grater than or equal to ), <=(less than or equal ))
logical operators( and: return True),( or : return True if at least one statement is True), (not: reverses the result (result False if the result is Ture))
 """

print("----Welcome to python basics demo program -----")

#2 variables $ input and data types
# user_name = input("Apna naam enter karein:")
# print("intput", user_name)

# num1 = float(input("pehala number (int/float) enter karein: "))
# num2 = float(input("doosra number (int/float) enter karien: "))

# # user se age lena aur use integer me badalna (type casting)

# age = int(input("apni age (saal me ) enter karein: "))

# #3 type checking (type())

# print("\n--- Data types used ---")
# print("user_name ka type hai:", type(user_name))
# print("num1 ka type hai: , type(num1)")
# print("age ka type hai:", type(age))


#arithimethic operators

# sum_result = num1 + num2 
# sum_result = num2 - num1 
# sum_result = num1 * num2
# sum_result = num3 / num4
# sum_result = num1 % num2

# print("\n ----- Arithmetic calculations -----")
# print(f"{num1} + {num2} = {sum_result}")
# print(f"{num1} - {num2} = {sum_result}")
# print(f"{num1} / {num2} = {sum_result}")
# print(f"{num1} * {num2} = {sum_result}")
# print(f"{num1} // {num2} = {sum_result}")
# print(f"Remainder job {num1} ko {num2} se divide karenge: { mod_result}")


#assigment opeeratures
counter = 10
counter += 5
print(f"\nAssignment operator example (10 += 5): { }")

#making a contact book using python ----- pythonnn----

contacts = {}

def Add_contact():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    Phone = input("Enter Phone number: ").strip()
    Email = input("Enter email:").strip()
    address = input("Enter address: ").strip()


    contacts[name] = {
        "Phone": Phone,
        "age": age,
        "email" : Email,
        "address": address
    }

    if len(Phone) != 10 or not Phone.isdigit():
        print("Error: Phone number must contain 10 digits")
        return 
    
    if name in contacts:
        print("Contact is already exists!")
        return
    print(f"contact '{name}' added successfully!")

def View_contact():
    if len(contacts) == 0:
        print("No contact found!")
    else:
        print("\n---- Your contact ----")

        for name, phone in contacts.items():
            print("Name:", name)
            print("Phone:", phone)
            print("age:", age)
            print("Email:", email)
            print("address:", address)
            print("-----------")


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]["Phone"])
        print("age:", contacts[name]["age"])
        print("email:", contacts[name]["email"])
        print("address:",contacts[name]["address"])

    else:
        print("contact not found!.")

def Delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name, age, email, address]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def updated_contact():
    name = input("Enter update name: ")

    if name in contacts:

        pass

    else:
        print("Contact not found!")



while True:
    print("\n=======CONTACT BOOK =======")
    print("1.ADD Contact")
    print("2.View Contacts")
    print("3.search Contacts")
    print("4.Delete Contacts")
    print("5.Update contact")
    print("6. Exit")


    choice = int(input("Enter choice (1-5): "))

    if choice == 1:
        Add_contact()

    elif choice == 2:
        View_contact()
    
    elif choice == 3:
        search_contact()

    elif choice == 4:
        Delete_contact()

    elif choice == 5:
        updated_contact()

    elif choice == 6:
        print("Thank you for using contact book!")
        break
    
else:
    print("Good byee come later!.")



class coffee:

    def __init__(self, name, price):
        self.name = name
        
        self.price = price

    
    def __init__(self):

        self.items = []
        
    
    def  add_item(self, coffee):

        self.items.append(coffee)

        print(f"Added {coffee.name} to your order.")
        
    #calculating total price

    def total(self):

      return sum(item.price for item in  self.items)

#show order summary
    
    def show_order(self):

        if not self.items:

             print("No items in order.")

             return

        print("\nYour order: ")

        for i ,item in enumerate(self.items, 1):

            print(f"{i}. {items.name} - ${item.price}")

        print(f"{i}.{item.name} - ${item.price}")

        



# class Student:
#     collage_name = "anbx"
# mylist = [10,20 , 30]
# print(mylist,type(mylist))
# mylist = [10, 20 , 30]
# print(mylist[len(mylist)] -1)

# mylist = [10, 20, 30, "asd", 7.0, 8+8j,[1,3,4]]
# print(mylist)
# mylist = [10, 40, 30]
# last = mylist.pop()
# print(last)
# print(mylist)

# mylist = []


# n = int(input())
# for i in range(n):
#     currEle = int(input())
#     mylist.append(currEle)

# print(mylist)
# mylist = input().split(" ")
# for i in range(len(mylist)):
#     mylist[i] = int(mylist[i])

# print(mylist, type(mylist))

# mylist = input().split(" ")
# for i in range(len(mylist)):
#     mylist[i] = int(mylist[i])

# print(mylist.type(mylist))


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


             


             
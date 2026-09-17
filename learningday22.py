# class Student:
#     collage_name = "abca collage"
#     # name = "Karan"
#     def __init__(self, name, marks):
#       self.name = name 
#       self.marks = marks

#     def welcome(self):
#       print("Welcome student,", self.name)

#     def get_marks(self):
#       return self.marks

#       # print("adding new student in database..")
        

# s1 = Student("karan", 90)
# s1.welcome()
# print(s1.get_marks)
# print(s1.name, s1.marks)

# s2 = Student("arjun",99)
# print(s2.name, s2.marks)
# print(s1.collage_name)

# class Car:
#     color = "blue"
#     color = "red"
#     brand = "mercedes"
#     brand = "BMW"


# Car1 = Car()
# print(Car1.color)
# print(Car1.brand)

# class student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#           sum += val 
#         print("hi", self.marks, "Your avg score is:", sum/3)

# s1 = student("tony stark", [99, 98 ,97])
# s1.get_avg()
# s1.hello()

# s1.name = "ironman"
# s1.get_avg()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc


    #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs." , amount, "was debited")
#         print("total balance = ", self.get_balance())


#     def credited(self, amount):
#         self.balance += amount
#         print("Rs." , amount, "was credited")
#         print("total balance = ", self.get_balance())


#     def get_balance(self):
#         return self.balance
  

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.credited(5000)
# acc1.debit(10000000000000)
        
# class Student:
#     def __init__(self, name):
#        self.name = name

    
# s1 = Student("sumit")
# # print(s1.name)
# del s1.name
# print(s1.name)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no  = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1  = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())
        
# class Person:
#     __name = "anonymous"

#     def __hello():
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# # print(p1.__hello())

# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyotacar(Car):
#     def __init__(self, brand):
#         self.brand = brand
#         # self.name = name

# # car1 = Toyotacar("fortuner")
# # car2 = Toyotacar("prius")

# # print(car1.start())
# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("diesel")
# car1.start()

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Simple Quiz Game
print("What is the capital of india?")
print("1 Delhi")
print("2 Mumbai")
print("3 haryana")
print("4 Uttar pradesh")

user_choice = input("Choose number btw 1- 4: ")
score = 0

if user_choice == "1":
    print("Correct answer")
    score += 1
      
else:
    print("Incorrect answer")

print("What is the know as pink city?")
print("1 Delhi")
print("2 jaipur")
print("3 haryana")
print("4 Uttar pradesh")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "2":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
   

print("What is the national bird of india?")
print("1 peakcook")
print("2 sparrow")
print("3 owl")
print("4 crow")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "1":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    

print("What is the short form of central processing unit?")
print("1 RAM")
print("2 GPU")
print("3 CPU")
print("4 USC")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "3":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
  

print("What is the Prime minister of india?")
print("1 Pm modi")
print("2 Rahul gandhi")
print("3 bhajpa")
print("4 chai wala")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "1":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")

print("you got" +str(score) + "question correct!")
print("You got" + str((score / 5) * 100) + "%.")
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
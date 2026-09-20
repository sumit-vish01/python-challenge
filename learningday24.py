# class Car:
#         def __init__(self, type):
#             self.type = type

#         @staticmethod
#         def start():
#          print("car started..")

#         @staticmethod
#         def stop():
#           print("car stopped.")

# class Toyotacar(Car):
#         def __init__(self, name, type):
#           self.name = name
#           super().__init__(type)

# car1 = Toyotacar("prius", "electric")
# print(car1.type)


# class Person:
#     name = "Anonymous"

#     # def changeName(self, name):
#     #     self.__class__.name = "Rahul"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math  = math
#         # self.percentage = str((self.phy + self.chem + self.math)/ 3 ) + "%"


#     @property
#     def percentage(self):
#         return ((self.phy + self.chem + self.math)/ 3 ) + "%"


# stu1 = Student(98, 97, 97)
# print(stu1.percentage)

# # stu1 = Student(98, 93,92)
# # print(stu1.percentage) 

# stu1.phy = 89
# print(stu1.percentage)

# polymorphism

# print("apna +collage")
# print(type("apna"))

# print([1, 2, 3] + [4, 5, 6])
# print(type([1, 2, 3]))

# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img


#     def showNumber(self):
#         print(self.real, "i +", self.img ,"j")


#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newReal, newimg)


#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newimg = self.img - num2.img
#         return complex(newReal, newimg)

# num1 = complex(1, 3)
# num1.showNumber()

# num2 = complex(4, 8)
# num2.showNumber()

# # num3 = num1.add(num2)
# # num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()

# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7)*self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7)* self.radius


# c1 = circle(21)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showdetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary=", self.salary)

# class Engineer(Employee):
#     def __init(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "ITI", "78,000")

# # e1 = Employee("accountant", "Finacne", "60,000")
# # e1.showdetails()

# engg1 = Engineer("Elon Musk", 40)
# engg1.showdetails()

# class order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price


#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr1 = order("chips", 20)
# odr2 = order("tea",15)

# print(odr1 > odr2)
    

# #from zero se advace level tak 

# print("hello")
# print(10)
# print(10 + 20)

# name = "sumit"
# age = 29

# print(name, age)

# print(f"My name is {name} and my age is {age}")

# int = 10
# float = 12.00
# complex = 2 +3j

# str = "whllp"
# bool = True
# list = [1, 2, 3]
# tuple = (1, 2,3 )
# set = {1, 2,3 }
# dict = {"name":, "sumit"}
# nonetype = none

# x = 20
# print(type(x))
#type conversion

# x = "10"
# y = int(x)

# print(y)
# x = 10
# y = str(x)

# x ="10.5"
# y = float(x)

# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool("hellp"))
# #input

# name = input("Enter your name: ")
# print(name)
# age = input("Enter your age: ")
# print(type(age))

#operators

# a = 10
# b = 4

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

#comparison operators

# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

#logical operators 

# age = 20
# print(age >= 18 and age <= 60)

# age = 20
# print(age < 19 or age > 60)

# print(not True)

#assignmet operatures
# z =100
# y = 20

# z += 5
# z -= 2
# z *= 3
# z /= 2

#if elif , and else:

# marks = 200

# if marks >= 120:
#     print("pass")
# else:
#     print("fail")

# marks = 85

# if marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("c")
# else:
#     print("Fail")

#nested condition

# age = 20

# if age >= 19:
#     if age <= 60:
#         print("Adult")


# if 18 <= age <= 60:
#     print("Adult")

# name = ""

# if name:
#     print("Name exists")
# else:
#     print("Empty")

#loops

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# i = 1

# while i <= 90:
#     print(i)
#     i += 2

#for loop

# for i in range(5):
#     print(i)

# for i in range(1 , 20 , 5):
#     print(i)

# for i in range(1 , 10):
#     if i == 5:
#         break 
#     print(i)

#continue

# for i in range(1 , 6):
#     if i == 3:
#         continue
#     print(i)

# if True:
#     pass

#strings

# name = "python"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[-3])

#string slicing

# test = "pyhton"
# # print(test[0:3])
# print(test[:3])
# print(test[2:])
# print(test[::-1])
# text = "HEllo world"

# # text.upper()
# # text.lower()
# # text.capitalize()
# print(text.replace("world","python"))
# # print(text)
# text = "sumit vishwakarma"
# # print(text.split())
# print(" ".join(text))

# words = ["I", "love","python"]

# # print(" ".join(words))
# print(words.strip)

# name ="smit vishwakarma"
# # # print(name.strip())
# # # print(name.find("sumit"))
# # print(name.count("i"))

# print("python".startswith("vi"))
# print("python".endswith("ma"))

#string immutability

# name = "python"
# # name[0] = "j"
# name ="j" + name[1:]

# #lists 
# numbers = [10, 20, 30, 40]

# print(numbers[0])
# numbers[0] = 100
# print(numbers)

# list = [10, 20, 30, 40]

# print(list.append(50))
# # print(list.insert(1, 15))

# words = [10, 20, 30, 40]
# # words.append(50)
# # words.insert(1, 15)
# # words.remove(20)
# # words.pop()
# # words.pop(1)
# # words.sort()
# words.reverse()
# # words.clear()
# print(words)

#list slicing

# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])

#list looping
# numbers = [10, 20, 30]

# # for num in numbers:
# #     print(num)

# for i in range(len(numbers)):
#     print(i, numbers[i])

# numbers = [10, 20, 30]

# # for i in range(len(numbers)):
# #     print(i , numbers[i])

# for i, num in enumerate(numbers):
#     print(i , num)
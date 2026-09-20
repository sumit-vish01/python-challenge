#starting from tuples
# point = (10, 20)
# point[0] = 50


# x, y = (10, 20)

# print(x)
# print(y)

#set
# numbers = {1, 2, 3,3, 4}
# print(numbers)
# numbers = {1, 2, 3,3, 4}
# # numbers.add(5)
# numbers.remove(2)
# print(numbers)

# a = {1,2,3}
# b = {3, 4, 5}

# # print(a| b)
# # print(a & b)
# print(a - b)

#dictionary

student = {
    "name": "sumit",
    "age": 18,
    "marks": 85

}
# print(student.get("name"))
# student["city"] = "palwal"
# student["marks"] = 90
# student.pop("age")
# student.keys()
# student.values()
# student.items()
# print(student)

# for key, value in student.items():
#     print(key, value)

# for value, key in student.keys():
#     print(value, key)

#functions
# def greet():
#     print("hello")

# greet()

#parameter and arguments

# def greet(name):
#     print("hello",name)

# greet("sumit")

# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)

#print() vs retun

# def add(a, b):
#     print(a + b)


# sumit = add(20, 40)


# def add(a, b):
#     return a + b

# sumit = add(100, 200)

#default arguments 

# def greet(name = "student"):
#     print("Hello", name)

# greet()
# greet("sumit")

#keyword arguments

# def student(name, age):
#     print(name, age)

# student(age= 18, name="sumit")

# def student(name, marks):
#     print(name, marks)


# student(name ="rahul", marks =200 )

# *args

# def add(*numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     return total
# print(add(1, 2))
# print(add(1,2,3,4))
# def info(**data):
#     print(data)

# info(name="sumit", age=18, city="Palwal")

#scope

# x =10

# def test():
#     x = 20
#     print(x)


# test()
# print(x)

#global 

# x = 10

# def change():
#     global x
#     x = 20

# change()
# print(x)

#lambda

# square = lambda x: x* x

# print(square(5))

# def square(x):
#     return x *x 

#map

# numbers = [1, 2,3,4]

# result = list(map(lambda x: x*2, numbers))

# print(result)

#filter()

# numbers = [1, 2,3,4,5]

# result = list(filter(lambda x: x % 2 == 0, numbers))

# print(result)

#list comprehesnsion

# squares = []

# # for i in range(1, 6):
# #     squares.append(i * i)

# squares = [i * i for i in range(1, 6)]

# print(squares)

# even = [i for i in range(10) if i % 2 == 0]
# print(even)

# squares = {i: i*i for i in range(1, 6)}
# print(squares)

# squares = {i: i*i for i in range(1, 6)}
# print(squares)

#nested data

# matrix = [
#     [1,2],
#     [3, 4]
# ]

# print(matrix[0][1])

# student ={
#     "name": "sumit",
#     "subject":["Maths", "Python","English"]
# }
# print(student)


#exception handling


# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("cannot divide by zero")

# try:
#     x = 9/2
# except ValueError:
#     print("it cannot predict")

#try-except-else-finally

# try:
#     num = int(input("Enter number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("valid numbes")
# finally:
#     print("Program Finished")

#multiple exceptions

# try:
#     a = int(input())
#     b = int(input())
#     print(a /b)

# except ValueError:
#     print("Enter numbers only")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

#raise

# age = -5

# if age < 0:
#     raise ValueError("age cannot be negative")

#file handling

# file = open("data.txt","r")

# content = file.read()
# print(content)

# file.close()

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

#write

# with open("data.txt","w")as file:
#     file.write("Hello python")

# with open("data.txt", "a") as file:
#     file.write("\nNew line")

# with open("data.txt", "a") as file:
#     file.write("\nNew line")

#json

# import json

# # student = {
# #     "name": "Sumit",
# #     "age": 19
# # }

# # with open("student.json","w") as file:
# #     json.dump(student, file)

# with open("student.json","r") as file:
#     data = json.load(file)

# print(data)

#modules

# import math

# print(math.sqrt(25))
# print(math.pi)

# import math as m

# print(m.sqrt(25))

# import random
# print(random.randint(1, 10))

# from datetime import datetime

# now = datetime.now()
# print(now)

# from datetime import datetime

# now = datetime.now()
# print(now)
#os

# import os

# # print(os.getcwd())

# print(os.listdir())

# import os

# os.mkdir("test")

#object oriented programming --oop

# class student:
#     def __init__(self):

#      s1= student()

#constructor

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# s1 = student("sumit", 19)
# print(s1.name)
# print(s1.age)

# class student:
#     def __init__(self, name):
#         self.name = name


# s1 = student("sumit")
# s2 = student("Rahul")

# class student:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)

# s1 = student("sumit")
# s1.show()

#class variable

# class student:
#     collage = "Sr collage"

#     def __init__(self, name):
#       self.name = name        

# # print(student.collage)
# s1 = student("Sumit")
# print(s1.collage)

#encapsilation

# class student:
#     def __init__(self):
#         self.name = "sumit"  #public
#         self._branch = "CSE"  #protected convention
#         self.__marks = 90     #privet name - mangling

#getter/ setter with property

# class student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#      return self._marks

#     @marks.setter
#     def marks(self, value):
#        if 0<= value <= 100:
#         self._marks = value
#       else:
#           raise vars

    

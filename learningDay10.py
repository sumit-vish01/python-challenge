# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print('Division successful:', x)
# finally:
#     print('This block always runs.')

# try:
#     number = int('abc')
#     result = 10 / number
# except ValueError:
#     print('That was not a valid number.')
# except ZeroDivisionError:
#     print("Can't divide by zero.")

# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f'Error occurred: {e}')

# try:
#     number = int(input('Enter a number: '))
#     result = 10 / number
# except (ValueError, ZeroDivisionError) as e:
#     print(f'Error occurred: {e}')


# def check_age(age):
#     if age < 0:
#         raise ValueError('Age cannot be negative')
#     return age

# try:
#     check_age(-5)
# except ValueError as e:x
#     print(f'Error: {e}') # Error: Age cannot be negative


 #revision


#variables

# name = "sumit"  string
# age = 18  integer
# marks = 90.9  float
#price = 99  float
#passed = True  boolean
# print(name)
# print(age)

# name = input("Enter your name: ")
# print("hello", name)

# age = int(input("Enter your age:"))

# print("your age is " ,age)

#operatures 

# a = 19
# b = 6

# print(a + b)
# print(a - b)
# print(a * b)
# print(a  /b)
# print(a  %b)
# print(a  //b)
# print(a  **b)


#if else

# age =16

# if age >= 18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

#elif 

# marks = 90
# if marks >= 90:
#     print("A+")
# elif marks >= 75:
#     print("A")
# elif marks >=68:
#     print("B")
# else:
#     print("C")

#loops (ka use same kaam ko baar baar karne ka liye use hota hha)

# for i in range(6):
#     print(i)

# for i in range(1, 6):
#     print("Hello")

#while loop

# count = 1


# while count <= 100:
#     print(count)
#     count = count + 9

# count = 9



# while count <= 400:
#     print(count)
#     count = count + 90


#list (list me multiple value ko store karte ha )

# fruits = [ "apple", "Banan", "Mango"]


# fruits.append("orange")
# print(fruits)
# print(fruits[0])


#functions (ek reusable piece of code hota hai)

# def greet(name):
#     print("hello",name)


# greet("Sumit")
# def greet(name):
#     print("hello yrr are u fine", name)

# greet("Rahul")

# def add(a, b):
#     return a + b

# # result = add(10, 20)

# # print(result)

# marks = add(30, 50)
# print(marks)


#dictionarise(me key:value hota ha )

# student = {
#     "name" : "sumit",
#     "age" : 19,
#     "marks" :89
# }

# print(student["name"])
# print(student["marks"])

#student marks calculators

# def calculate_result():
#     name = input("Enter student name:")

#     math = float(input("Enter Maths marks:"))
#     python = float(input("Enter Python marks:"))
#     english = float(input("Enter English marks:"))

#     total = math + python + english
#     percentage = total / 3

#     print("in--- Result---")
#     print("Name:",name)
#     print("Total:", total)
#     print("Percentage:",percentage)


#     if percentage >= 90:
#         print("Grade: A+")
#     elif percentage >= 80:
#         print("Grade: A")
#     elif percentage >= 70:
#         print("Grade: B")
#     elif percentage >= 60:
#         print("Grade: C")
#     else:
#         print("Grade: D")

# calculate_result()

tasks = []


while True:
    print("\n--- To Do LIST ---")
    print("1 Add task")
    print("2 View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1"
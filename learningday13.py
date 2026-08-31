# num = 10
# print(num / 0)

#try and expect 

# try:
#     num = 10
#     result = num / 0
#     print(result)

# except:
#     print("something went wrong")
# try:
#     num = 10
#     result = num / 0

# except ZeroDivisionError:
#     print("You cannot divide by zero")

#value error

# try:
#     age = int(input("Enter your age:"))
#     print("your age is :",age)

# except  ValueError:
#     print("PLesase enter a valid number")

# try:
#     a = int(input("enter first number:"))
#     b = int(input("enter second number:"))

#     print(a / b)

# except ValueError:
#     print("please enter numbers only:")

# except ZeroDivisionError:
#     print("cannot divide by zerO")

# try:
#     num = int(input("Enter a number :"))
#     result = 10 / num
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print("answer:", result)

# def check_age(age):
#     if age < 0:
#         raise ValueError('age cannot be negative')
#     return age

# try:
#     check_age(-5)
# except ValueError as e:
#     print(f'error: {e}') # error : age cannot be negative

# def process_data(data):
#     try:
#         result = int(data)
#         return result * 2
#     except ValueError:
#         print('logging: invalid data received')
#         raise # re - raise the same valueerror

# try:
#     process_data('abc')
# except ValueError:
#     print('handled at higher level')

# class insufficientfundserror(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount 
#         super().__init__(f'insuuficient funds: ${balance} available, ${amount} requested')

# def withdraw(balance,amount):
#     if amount > balance:
#         raise insufficientfundserror(balance, amount)
#     return balance - amount 

# try:
#     new_balance = withdraw(100, 150)
# except insufficientfundserror as e:
#     print(f' transaction failed: {e}')

# def parse_config(filename):
#   try:
#     with open (filename, 'r') as file:
#       data = file.read()
#       return int(data)
#   except FileNotFoundError:
#     raise ValueError('configuration file is missing') from None
#   except ValueError as e:
#     raise ValueError('invalid configuration format') from e 

# # config = parse_config('config.txt')
# def validate_isbn(isbn, length):
#     if len(isbn, length) != length:
#         print(f'ISBN-{length} code should be {length} digits long.')
#         return
#     main_digits = isbn[0:length]
#     given_check_digit = isbn[length]
#     main_digits_list = [int(digit) for digit in main_digits]
#     # Calculate the check digit from other digits
#     if length == 10:
#         expected_check_digit = calculate_check_digit_10(main_digits_list)
#     else:
#         expected_check_digit = calculate_check_digit_13(main_digits_list)
#     # Check if the given check digit matches with the calculated check digit
#     if given_check_digit == expected_check_digit:
#         print('Valid ISBN Code.')
#     else:
#         print('Invalid ISBN Code.')
# def calculate_check_digit_10(main_digits_list):
#     # Note: You don't have to fully understand the logic in this function.
#     digits_sum = 0
#     # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
#     for index, digit in enumerate(main_digits_list):
#         digits_sum += digit * (10 - index)
#     # Find the remainder of dividing the sum by 11, then subtract it from 11
#     result = 11 - digits_sum % 11
#     # The calculation result can range from 1 to 11.
#     # If the result is 11, use 0.
#     # If the result is 10, use upper case X.
#     # Use the value as it is for other numbers.
#     if result == 11:
#         expected_check_digit = '0'
#     elif result == 10:
#         expected_check_digit = 'X'
#     else:
#         expected_check_digit = str(result)
#     return expected_check_digit
# def calculate_check_digit_13(main_digits_list):
#     # Note: You don't have to fully understand the logic in this function.
#     digits_sum = 0
#     # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
#     for index, digit in enumerate(main_digits_list):
#         if index % 2 == 0:
#             digits_sum += digit * 1
#         else:
#             digits_sum += digit * 3
#     # Find the remainder of dividing the sum by 10, then subtract it from 10
#     result = 10 - digits_sum % 10
#     # The calculation result can range from 1 to 10.
#     # If the result is 10, use 0.
#     # Use the value as it is for other numbers.
#     if result == 10:
#         expected_check_digit = '0'
#     else:
#         expected_check_digit = str(result)
#     return expected_check_digit
# def main():
#     user_input = input('Enter ISBN and length: ')
#     values = user_input.split(',')
#     isbn = values[0]
#     length = int(values[1])
#     if length == 10 or length == 13:
#             validate_isbn(isbn, length)
#     else:
#        print('Length should be 10 or 13.')

# main()


# def calculate(a, b):
#     return a + b ,a - b

# x , y = calculate(40, 10)
# print(calculate)
#scope = variable kahan accessible hai

# def test():
#     x = 10
#     print(x)

# x = 10

# def change():
#     global x 
#     x = 20

#syntax error

# if True: 
#     print("hello")

#logical error
# a = 10
# b = 20
# print( a - b)
#try except else finally
# try:
#     x = int(input("enter number:"))
#     print(10/ x)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("cannot divide by zero")

#else:

# try:
#     x = int(input("enter number:"))
# except ValueError:
#     print("invalid")
# else:
#     print("valid input")

# try:
#     x = int(input("Enter number:"))
# except ValueError:
#     print("invalid")
# else:
#     print("valid input")

# try:
#    print("hello")
# except:
#    print("error")
# finally:
#    print("always runs")


#file handling
# file = open("file.txt", "r")

#module 

# import math

# print(math.sqrt(25))

# import math

# print(math.sqrt(25))
# print(math.ceil(4.2))
# print(math.floor(4.8))

# import random 
# number = random.randint(1, 10)
# print(number)

#calculator .py
# import calculator
# # def add(a, b):
# #     return a + b


# print(calculator.add(10, 20))

# a = 10
# b = 20

# print("a=", a)
# print("b=",b)

# result = a + b
# print("result =", result)

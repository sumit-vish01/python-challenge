# numbers = [112, 3, 4,5]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# secret_numbers = 5
# guess = 0

# while guess != secret_numbers:
#     guess = int(input('guess the number (1-5):'))
#     if guess != secret_numbers:
#         print('wrong! Try again.')

# print('you got it!')

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#      continue
#     print(developer)

# for num in range(2, 11, 2):
#     print(num)

# languages = ['sapnish','English','Russsian','Chinese']

# for index, language in enumerate(languages):
#     print(f'Index {index} and language {language}')

# even_numbers = [num for num in range(21) if num % 2 ==0]
# print(even_numbers)

# words = [ 'trees','sky','mountain','river','cloud','sun']
# def is_long_word(word):
#     return len(word) > 4
# long_word = list(filter(is_long_word, words))
# print(long_word)

# celsius = [ 0, 10, 20, 30, 40]
# def t0_fahrenheit(temp):
#     return (temp * 9/5) + 32

# fahrenheit = list(map(t0_fahrenheit,celsius))
# print(fahrenheit)

# n = [ 5, 10, 15, 20]
# total= sum(n,start= 10)
# print(total)

# numbers = [ 1, 2,3 ,4,5]
# even_number = list(filter(lambda x: x%2 == 0, numbers))
# print(even_number)
# cities = ['Los Angeles', 'London', 'Tokyo']
# print(cities[-1])
# developer = 'Jessica'

# print(list(developer))
# desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
# print(desserts[1:3])
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 8, 10]

# numbers.extend(even_numbers)
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 5, 5]
# numbers.remove(5)

# print(numbers)
# developer = ('Jane Doe', 23, 'Python Developer')
# del developer[1]
# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# programming_languages.index('Python', 3)
# print(programming_languages)
# developer = ('Jane Doe', 23, 'Python Developer')
# del developer[1]
# numbers = [1, 2, 3, 4, 5, 5, 5]
# numbers.remove(5)

# print(numbers)
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 8, 10]

# numbers.extend(even_numbers)
# print(numbers)
# desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
# print(desserts[1:3])
# pizza = dict([('name', 'Margherita Pizza'),
# ('price', 8.9), 
# ('calories_per_slice', 250), 
# ('toppings', ['mozzarella', 'basil'])])
# print(pizza)
# dictionary.get(key,delfault)
# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250
# }
# # # print(pizza)
# # # pizza.keys()
# # pizza.values()
# pizza.update({ 'price': 15, 'total_time': 25 })
# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# for price in products.values():
#     print(price)

# for index, product in enumerate(product.items()):
#     print(index,product)
# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# for product in products.items():
#     print(product)
# my_set = {1, 2, 3, 4, 5, 6}
# my_set.add(5)

# print(my_set)
# try:
#     print(22 /0)
# except ZeroDivisionError:
#     print('You can\'t divide by zero!')

# try:
#     number = int(input('Enter a number: '))
#     print(22/ number)
# except ZeroDivisionError:
#     print('You cannot divide by zero!')
# except ValueError:
#     print('Please enter a valid number!')

# try:
#     result = 100/ 4
# except ZeroDivisionError:
#     print('You cannot divide by zero!')
# else:
#     print(f'Result is {result}')
# finally:
#     print('exception completely')

# try:
#     value = int('this willrasie an error')
# except ValueError as e:
#    print(f'Caught an error:{e}')
   

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('you cannot divide eith zero')
#     return a / b

# class InvalidcredentialError(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)

# class InvalidcredentialError(Exception):
#     def __init__(self, message="Invalid username or password"):
#         self.message = message
#         super().__init__(self.message)

# def login(username, password):
#     stored_uername ="admin"
#     stored_password = "password"

#     if username != stored_uername or stored_password != stored_password:
#         raise InvalidcredentialError()

#     return f"Welcome, { username}"

# def parse_config(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#             return int(data)
#     except FileNotFoundError:
#         raise ValueError('Configuration file is missing') from None
#     except ValueError as e:
#         raise ValueError('Invalid configurates format') from e

#     config = parse_config('config.txt')
# try:
#   print(22 / 0)
# except ZeroDivisionError:
#   print("You can't divide by zero!")
# print("Hello world"

# class className:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

# def sample_method(self):
#     print(self.name.upper())

# class Dog:
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age 

# def bark(self):
#     print(f"{self.name.upper()} says woof woof!")

# class Dog:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says woof woof! I'm{self.age} years old!")


# dog_1 = dog("Jack", 3) 
# dog_2 = dog("thatcher", 5)
#         pass
# class Dog:  
#     def __init__(self, name):  
#         self.name = name

#     def bark(self):  
#         print(f"{self.name} says Woof!")  

# my_dog = Dog("Rex")
# print(my_dog.name)
# class Dog:
#     species = "French Bulldog"

#     def __init__(self, name):
#         self.name = name

# print(Dog.species)

# dog1 = Dog("Jack")
# print(dog1.name)
# print(dog1.species)

# dog2  = Dog("jack")
# print(dog1.name)
# print(dog1.species)

# dog2 = Dog("Tom")
# print(dog2.name)
# print(dog2.species)

# class car:
#     def __init__(self,color,  model):
#         self.color = color 
#         self.model = model

# car_1 = car("red", "toyota corolla")
# car_2 = car("green","lambhorgingi Revolution")

# print(car_1.model)
# print(car_2.model)

# print(car_1.color)
# print(car_2.color)
        
# class Car:
#     def __init__(self, color, model):
#         self.color = color  # Instance attribute
#         self.model = model  # Instance attribute

#     def describe(self):
#         return f"This car is a {self.color} {self.model}"

# car_1 = Car("red", "Toyota Corolla")
# car_2 = Car("green", "Lamborghini Revuelto")

# print(car_1.describe()) # This car is a red Toyota Corolla
# print(car_2.describe()) # This car is a green Lamborghini Revuelto


#file I/O in python 
# file = open("data.txt", "r")

# data = file.read

# print(data)

# file.close()

# f = open("data.txt","r+")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# with open("data.txt","r") as file:
#     data = file.read()
#     print(data)
#readlines ek baar me bas ek line read krta ha

# with open("data.txt","r") as file:
#    print(file.readline())
#    print(file.readline())
#    print(file.readline())
#    print(file.readline())

# with open("data.txt","r") as file:
#     lines = file.readlines()

#     print(lines)

# with open("data.txt","r") as file:
#     lines = file.readlines()

#     print(lines)


# with open("data.txt", "w") as file:
#     file.write("Hello python")

# with open("data.txt","w") as file:
#     file.write("Hello how are u  and thanks for ansking that things")


# with open("data.txt","w") as file:
#     file.write("Hello world")

# with open("data.txt","w") as file:
#     file.write("python\n")
#     file.write("C++\n")
#     file.write("Java\n")

#append  existing  data ka end me naya data add karna

# with open("data.txt","a") as file:
#     file.write("\nJava")


# Name = open("Enter your name")
# with open()
# f = open("sample.txt","a")
# f.close()

# import os

# os.remove("data.txt")

# with open("practice.txt","w") as file:
#     file.write("Hi everyone\nwe are learning fileI/o\n")
#     file.write("using java.\nI like programming in java.")
    
# with open("practice.txt","r") as file:
#     data = file.read()

# new_data = data.replace("Java", "python")
# print(new_data)

# with open("practice.txt","w") as file:
#     file.write(new_data)

# class Book:
#     def __init__(self, title , pages):
#         self.title  = title
#         self.pages = pages

# book1 = Book("Built Wealth like a Boss", 420)
# book2 = Book("Be Your Own start", 420)

# # print(len(book1))
# print(str(book1))
# print(book1 == book2)

# class Book:
#     def __init__(self, title , pages):
#         self.title = title
#         self.pages = pages

#     def __len__(self):
#         return self.pages
#     def __str__(self):
#         return f"'{self.title}' has {self.pages} pages"
#     def __eq__(self, other):
#         return self.pages == other.pages

# book1 = Book("BUilt wealth like a Boss", 420)
# book2 = Book("Be your Own start", 420)

# print(len(book1))
# print(len(book2))
# print(str(book2))
# print(book1 == book2)

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add(self, item):
#         self.items.append(item)

#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print(f'{item} is not in cart')

#     def __len__(self):
#         return len(self.items)

#     def __getitem__(self, index):
#         return self.items[index]

#     def __contains__(self, item):
#         return item in self.items

#     def __iter__(self):
#         return iter(self.items)

#     def list_items(self):
#         return self.items


# cart = Cart()
# cart.add('laptop')
# cart.add('Wireless mouse')
# cart.add('Ergo Keyboard')
# cart.add('Monitor')

# for item in cart:
#     print(item, end=' ')

# print(len(cart))
# print(cart[3])

# print('Monitor' in cart)
# print('Banana' in cart)

# cart.remove('Ergo Keyboard')

# print(cart.list_items())

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model 

# my_car = Car('Lamborgini','Gallardo')
# print(my_car.brand)
# print(my_car.model)

# # getattr(object, attribute_name, default_value)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person('John Doe', 30)

# print(getattr(person,  'name'))
# print(getattr(person,  'age'))
# print(getattr(person,  'city'))

# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 

# person = Person('John Doe', 30)

# attr_name = input('Enter the attribute you want to see: ')
# print(getattr(person, attr_name, 'Attribute not found'))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person = Person('John Doe', 30)

# att_name = input('Enter the attribute you want to see:')
# print(getattr(person, att_name, 'Attribute not found'))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person = Person('John Doe', 30)

# for attr in dir(person):
#     for attr in dir(person):
#         if not attr.startswith('__') and not callable(getattr(person, attr)):
#             value = getattr(person, attr)
#             print(f'{attr}: {value}')

# class Product:
#     def __init__(self,name, price):
#         self.name = name
#         self.price = price

# Product_a =Product('T-shirt',25)
# required_attributes = ['name','price','price']

# for attr in required_attributes:
#     if not hasattr(Product_a, attr):
#         # print('" Error: Product is missing the required attributes:'{attr}''
#         print(f"ERROR: PRoduct is missing the requirwed the reuired attributes:{attr}")
#     else:
#         print(f'{attr}: {getattr(Product_a,attr)}')

# class usersession:
#     def __init__(self, user_id, token):
#         self.user_id = user_id
#         self.auth_token = token
#         self.tenp_counter = 0

# session = usersession(101,'a1b2c3d4e5')

# for attr in attributes_to_clean:

        

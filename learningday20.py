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

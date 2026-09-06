# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = parameters

#     def method_name(self):
#         pass


# class car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# car1 = car('Toyota','red')
# car2 = car('Lambo','green')

# print('car 1 brand:', car1.brand)
# print('car 1 color:', car1.color)

# print('car 2 brand:', car2.brand)
# print('car 2 color:', car2.color)

# class Wallet:
#     def __init__(self, balance):
#       self._balance = balance

#     def deposit(self, amount):
#        if amount > 0:
#           self._balance+= amount

#     def withdraw(self, amount):
#        if 0 < amount <= self._balance:
#           self._balance -= amount


# class Wallet:
#     def __init__(self):
#         self.__balance = 0
#     def _validate(self, amount):
#         if amount <0:
#             raise ValueError('Amount must be positive')  
#     def deposit(self, amount):
# #         self.__validate(amount) 
# #  ise ValueError('Insufficient funds')   
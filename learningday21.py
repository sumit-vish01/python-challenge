# class classname:
#   def __init__(self, parameters):
#     attribute = Value

# def method_name(self):
  
# class Circle:
#     def __init__(self, radius):
#       self._radius = radius

#     @property
#     def area(self):
#       return 3.14*(self._radius**2)

#     @property
#     def area(self): 
#        return 3.14 *(self._radius**2)

# my_circle = Circle(3)

# print(my_circle._radius)
# print(my_circle.area)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def radius(self):
#         return self.radius

#     @radius.setter
#     def radius(self, value):
#         if value <= 0:
#             raise ValueError('Radius must be positive')
#         self.radius = value
# my_cicle = Circle(3)
# print('Initial radius ')
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self,}')
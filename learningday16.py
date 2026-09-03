# class Student:
#     name = "sumit"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "bmw"

# car1 = Car()
# print(car1.color) 
# print(car1.brand)

# class Student:

#     #default constructors
#     def __init__(self):
#         pass
# #parmeterized constructor

class Student:
    college_name = "ABC Collage"
    def __init__(self,fullname, marks):
       self.name = fullname
       self.marks = marks
       print(self)
       print("Adding new student in database..")

s1 = Student("sumit", 89)
print(s1.name, s1.marks)

s2 = Student("rahul",98)
print(s2.name,s2.marks)
 
print(s2.college_name)
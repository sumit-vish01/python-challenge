print("hello", end= " ")
print("world")

print("hello\nworld")

print("he said that \"world\"")
# print("He said \"Hello\"")
print("newone \"becxxx\"")

a,b,c =10,20,50
print(a,b,c)

a = 2+8j
n = 9 +4j
print(a+ n)

a, b = input("Enter two numbers: ").split()
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
a = 10
b = 20
c = 15

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

s = 90
b = 8
c= 800

if a >= b:
    print(c)
elif a ==b and b>= c:
    print(a)
else:
    print(c)
total = 0

for i in range(1, 6):
    total += i

print(total)

sum = 899

for i in range(3):
    sum += 2000

print(sum)

num = 5

for i in range(1, 11):
    print(num, "*", i, "=", num * i)


n = 10

for i in range(1, 1000):
    print(n, "*", i,"=", n * i   )

n = 9

for i in range(1, 100):
    print(n, "*", i,"=",n * i)

i = 1

while i <= 5:
    print(i)
    i += 1

i = 10

while i <= 100:
    print(i)
    i += 1

for i in range(1, 10):
    if i ==5:
        break
print(i)


for i in range(1, 10):
    if i == 5:
        break 
    print(i)

for i in range(1, 100):
    if i == 90:
        continue
    print(i)

words = "python"

print(words[0:11])
print(words[-9:-2])
print(words[:])
print(words[:-8])

a = "hwllo"
b = "world"

# print(a + " " + b)
print("hi " * 3)

n = input("enter your name:")
print("i Love you baby  " * 1000000000000)


# text.upper()
# text.lower()
# text.strip()
# text.replace("a", "b")
# text.split()

name  = "  sumit  "
print(name.strip())

text = "python programming"

# print("python" in text)
text.find("program")

name = "sumit"

age= 19
print(f" my name is {name} and I am {age} years old.")

text = "python"
print(text[::-1])

# lists 

numbers = [10, 20, 30, 40]
# print(numbers[1:3])
numbers[0] = 200
print(numbers)
numbers = [10, 20, 30, 40]

# numbers.append(70)
# # numbers.insert(1, 16)
# numbers.remove(20)
# numbers.pop()
# numbers.reverse()
# numbers.sort()
# numbers.index(10)
numbers.count(10)
print(numbers)

numbers = [10, 20, 30]

# for num in numbers:
#     print(num)

for name in numbers:
    print(name)

# nested lists 

matrix = [
    [1, 3],
    [3,8]
]
print(matrix[0][1])

tupes = (10, 20, 30)

print(tupes[0])


tuples = (10, 30, 340)
# print(tuples.count(10))
print(tuples.index(10))

data = 10, 20, 30

a, b , c = (10, 20 , 30)

numbers = {1, 2, 4,5 }
# numbers.add(9)
numbers.remove(2)
print(numbers)

# union

a = {1, 2, 3}
b = {3, 4, 5}

# print(a |b )
# print(a & b)
print(a - b)
# dictionaries

student = {
    "name": "sumit",
    "age":19,
    "marks": 45
}
# # print(student["name"])
# # student["city"] = "palwal"
# # student["age"] = 19
# # del student["age"] 
# # student.keys()
# student.values()
# student.items()

# print(student)

for key,value in student.items():
    print(key,value)

def check_age(age):
    if age < 0:
        raise ValueError('age cannot be negative')
    return age

    try:
        check_age(-5)
    except ValueError as e:
        print(f' errror ')
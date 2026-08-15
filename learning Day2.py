file = open('file.txt.txt', 'r')
f = file.readlines()

print(f)


list = 'sumit','newyork','powwerful'
list.find('t')
print(list)

text = "Welcome to Python programming"

if "Python" in text:
    print("Found!")
else:
    print("Not found!")


fruits =['banaa','papaya','sawberry','pineapple']

if 'banaa' in fruits:
    print('find out the banaa')

print(fruits.__format__('b'))

import math
import myModule


print(math.radians(90))
print(myModule.myfunc(6))

print(math.degrees(math.pi))

def func(x, text = '2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')

func('rx', '3')

  
